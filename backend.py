import sqlite3
from datetime import datetime as dt
import pandas as pd
import plotly.express as px
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
warnings.filterwarnings("ignore")


# Connect to the database
connection = sqlite3.connect('store.db', check_same_thread = False)

cursor = connection.cursor()

store = pd.read_pickle('store.pkl')
item_data = pd.read_pickle('items.pkl')
customer = pd.read_pickle('customers.pkl')
sales = pd.read_pickle('sales.pkl')

store['year'] = store['date_of_birth'].dt.year      # Adding Year of Birth
store['customer_age'] = 2022 - store['year']        # Adding customer age

def items():
    cursor.execute('SELECT * FROM items')
    data = cursor.fetchall()
    return data

def item_names():
    cursor.execute('SELECT name FROM items')
    item_names = cursor.fetchall()
    options = []
    for i in item_names:
        options.append(i[0])
    return options

names = item_names()

def total_sales():
    cursor.execute('SELECT SUM(price) FROM sales INNER JOIN items ON sales.item_id = items.id')
    total_sales = cursor.fetchone()
    return round(total_sales[0], 2)

def net_profit():
    cursor.execute('SELECT SUM(cost) FROM sales INNER JOIN items ON sales.item_id = items.id')
    cost = cursor.fetchone()
    cursor.execute('SELECT SUM(price) FROM sales INNER JOIN items ON sales.item_id = items.id')
    price = cursor.fetchone()
    profit = price[0] - cost[0]
    return round(profit, 2)

def total_orders():
    cursor.execute('SELECT COUNT(DISTINCT(sales_id)) FROM sales')
    total_orders = cursor.fetchone()
    return total_orders[0]

def best_selling_items():
    cursor.execute('SELECT name, COUNT(name) FROM items INNER JOIN sales ON items.id = sales.item_id GROUP BY name ORDER BY COUNT(name) DESC LIMIT 5')
    best_selling_items = cursor.fetchall()
    return dict(best_selling_items)

def least_selling_items():
    cursor.execute('SELECT name, COUNT(name) FROM items INNER JOIN sales ON items.id = sales.item_id GROUP BY name ORDER BY COUNT(name) ASC LIMIT 5')
    least_selling_items = cursor.fetchall()
    return dict(least_selling_items)

def basket():
    cursor.execute('''SELECT basket_sale_id, name, count(name) as item_count 
                    FROM sales INNER JOIN items ON items.id = sales.item_id GROUP BY basket_sale_id, name''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['basket_sale_id', 'name', 'item_count'])
    return df

basket_df = basket()

# print(basket_df.head(10))

def basket_consolidation(df):
    df['basket_sale_id'] = df['basket_sale_id'].astype('str')
    df = df.groupby(['basket_sale_id', 'name'])['item_count'].sum().unstack().reset_index().fillna(0).set_index('basket_sale_id')
    return df

# print(basket_consolidation(basket_df).head(10))

def one_hot_encoding(x):
    if(x <= 0):
        return 0
    if(x >= 1):
        return 1

basket_encoded = basket_consolidation(basket_df).applymap(one_hot_encoding)

bundling_algorithm = apriori(basket_encoded, min_support=0.05, use_colnames=True, low_memory=True)

bundling_rules = association_rules(bundling_algorithm, metric="confidence", min_threshold=0.1)

rules = bundling_rules[(bundling_rules['lift'] >= 1.2) & (bundling_rules['lift'] < 2.5)]

rules_list = rules.values.tolist()


def common_data(list1, list2):
    result = False
    # traverse in the 1st list
    for x in list1:
        # traverse in the 2nd list
        for y in list2:
            # if one common
            if x == y:
                result = True
                return result
    return result


def show_rules():
    for item in rules_list:
        # first index of the inner list
        # Contains base item and add item
        pair = item[0]
        items = [x for x in pair]
        # print(items)
        if len(items) > 1: 
            item1, item2 = items[0], items[1]
            print("Rule: " + item1 + " -> " + item2)
            # second index of the inner list
            support = item[4]
            print("Support: " + str(support))
            # third index of the list located at 0th position
            # of the third index of the inner list
            confidence = item[5]
            print("Confidence: " + str(item[5]))
            lift = item[6]
            print("Lift: " + str(item[6]))
            print("-----------------------------------------------------")


# show_rules()


def rec_dict():
    rec = dict()
    for item in rules_list:
        pair = item[0]
        items = [x for x in pair]    
        if len(items) > 1:
            item1, item2 = items[0], items[1]
            support = item[4]
            confidence = item[5]
            lift = item[6]
            if item1 not in rec.keys():
                rec[item1] = [item2, support, confidence, lift]
    return rec


recommendations_dict = rec_dict()


def show_recommendations(product):
    try:
        result = recommendations_dict[product]
        output = (
            f"\n"
            f"Recommended Item : {result[0]} \n \n"
            f"\n"
            f"Support : {result[1]} \n \n "
            f"Confidence : {result[2]} \n \n "
            f"Lift : {result[3]} \n "
            f"\n"
            f"It is recommended to bundle {product} with {result[0]}, since these two are frequently bought together."
            )
        return output
    except KeyError:
        output2 = f"Sorry, we don't have any recommendations for {product}."
        return output2



def monitoring():
    query = "SELECT name, (order_when - item_count) AS diff FROM items WHERE diff > 0"
    cursor.execute(query)
    data = cursor.fetchall()
    results = []
    for i in data:
        item_name = i[0]
        difference = i[1]
        # results.append(item_name, difference)
    df = pd.DataFrame(data, columns=['Items to Order', 'Quantity to Order'])
    return df



def bar_plot():
    series = store['date_of_birth'].dt.year
    x = series.value_counts()
    y = x.reset_index()
    y.columns = ['Year', 'Count']
    return y



def item_count():
    cursor.execute('''SELECT name, COUNT(name) FROM sales s INNER JOIN items i ON i.id = s.item_id 
                      INNER JOIN customers c ON c.id = s.customer_id GROUP BY name ''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['name', 'item_count'])
    return df



def year_cust_count():
    cursor.execute('''SELECT (2022 - STRFTIME('%Y', date_of_birth)) AS age, COUNT(STRFTIME('%Y', date_of_birth)) AS customer_count
                        FROM sales s INNER JOIN items i ON i.id = s.item_id INNER JOIN customers c ON c.id = s.customer_id 
                        GROUP BY age''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['year', 'customer_count'])
    return df




def sales_by_age():
    cursor.execute('''SELECT (2022 - STRFTIME('%Y', date_of_birth)) AS age, ROUND(SUM(price),2) AS total_sales
                    FROM sales s INNER JOIN items i ON i.id = s.item_id INNER JOIN customers c ON c.id = s.customer_id 
                    GROUP BY age''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['age', 'total_sales'])
    return df



def per_customer_sales():
    cursor.execute('''SELECT c.first_name, ROUND(SUM(price),2) AS total_sales
                    FROM sales s INNER JOIN items i ON i.id = s.item_id INNER JOIN customers c ON c.id = s.customer_id 
                    GROUP BY c.first_name ORDER BY c.first_name DESC''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['name', 'total_sales'])
    return df



def per_customer_items_sale():
    cursor.execute('''SELECT c.first_name, i.name, ROUND(SUM(price),2) AS total_sales
                    FROM sales s INNER JOIN items i ON i.id = s.item_id INNER JOIN customers c ON c.id = s.customer_id 
                    GROUP BY c.first_name, i.name''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['name', 'item_name', 'total_sales'])
    return df


def sales_per_hour():
    cursor.execute('''SELECT STRFTIME('%H', date_time) AS hour, ROUND(SUM(price),2) AS total_sales
                    FROM sales s INNER JOIN items i ON i.id = s.item_id INNER JOIN customers c ON c.id = s.customer_id 
                    GROUP BY hour''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['hour', 'total_sales'])
    return df



def sales_per_item():
    cursor.execute('''SELECT i.name, ROUND(SUM(price),2) AS total_sales
                    FROM sales s INNER JOIN items i ON i.id = s.item_id INNER JOIN customers c ON c.id = s.customer_id 
                    GROUP BY i.name''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=['item_name', 'total_sales'])
    return df
