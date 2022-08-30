import yaml
from backend import *
from styles import *
from plots import *

streamlit_style()

if st.session_state['validated'] == True:

    st.title(":bar_chart: Sales Dashboard")

    # TOP KPI's
    total_sales = total_sales()
    net_profit = net_profit()
    total_orders = total_orders()

    left_column, middle_column, right_column = st.columns(3)
    
    with left_column:
        st.subheader("Total Sales($)")
        st.subheader(f"{total_sales:,}")
    with middle_column:
        st.subheader("Net Profit($)")
        st.subheader(f"{net_profit:,}")
    with right_column:
        st.subheader("Total Orders")
        st.subheader(f"    {total_orders:,}")

    st.markdown("""---""")

    st.markdown("<h3 style='text-align: center; color: #468189;'>Best Selling Products</h3>", unsafe_allow_html=True)
    st.plotly_chart(plot_best_selling_items())

    st.subheader(" ")

    st.markdown("<h3 style='text-align: center; color: #468189;'>Least Selling Products</h3>", unsafe_allow_html=True)
    st.plotly_chart(plot_least_selling_items())

    st.subheader(" ")

    # st.markdown("<h3 style='text-align: center; color: #468189;'>Sales in Peak Hours</h3>",
    #             unsafe_allow_html=True)
    # st.plotly_chart(plot_sales_per_hour())

    st.subheader(" ")

    st.markdown("<h3 style='text-align: center; color: #468189;'>Per Customer Sales</h3>",
                unsafe_allow_html=True)
    st.plotly_chart(plot_per_customer_sales())

    st.subheader(" ")

    st.markdown("<h3 style='text-align: center; color: #468189;'>Sales by Customer Age Groups</h3>",
                unsafe_allow_html=True)
    st.plotly_chart(plot_sales_by_age())

    

else:
    st.title("Kindly Log In!!")

