from plots import *
from styles import *
from backend import *


streamlit_style()

if st.session_state['validated'] == True:
    st.title('📶 Bar Charts')
    st.markdown("""---""")
    
    st.subheader("Expand the tabs to see the plots")
    st.subheader(" ")

    with st.expander('Birth Year Count Plot'):
        st.plotly_chart(bar_plot_dob())
        st.write("The following chart represents the age ranges of customers in the data. Click on the age range to see the customers in that age range.")

    st.subheader(' ')
    with st.expander('Item Count Monitoring'):
        st.plotly_chart(item_count_plot())
        st.write("The following chart represents the count of Itemms in the data according to category.")

    st.subheader(' ')
    with st.expander('Age Group Segmentation'):
        st.plotly_chart(plot_year_cust_count())
        st.write("This Plot helps in figuring out the age group of most of the customers.")


else:
    st.title("Kindly Log In!!")
