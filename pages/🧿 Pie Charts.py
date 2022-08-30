from turtle import color
from plots import *
from styles import *
from backend import *


streamlit_style()

if st.session_state['validated'] == True:
    st.title('🧿 Pie Charts')
    st.markdown("""---""")
    
    st.subheader("Expand the tabs to see the plots")
    st.subheader(" ")

    with st.expander('Items Sunburst Plot'):
        st.plotly_chart(items_sunburst_plot())
        st.write("The following chart represents the categories in the items table. Click on the category to see the items in that category.")

    st.subheader(" ")

    with st.expander('Gender Pie Chart'):
        st.plotly_chart(gender_plot())
        st.write("This chart shows the Gender % count in the data.")

    st.subheader(' ')

    with st.expander('Items with Customers Sunburst Chart'):
        st.plotly_chart(cust_items_sunburst())
        st.write("This chart shows the Gender % count in the data.")

    st.subheader(' ')

    with st.expander('Item Category preference by Age Groups'):
        st.plotly_chart(category_sunburst())
        st.write("This the date of birth of customers and what's their preferred item category.")

else:
    st.title("Kindly Log In!!")