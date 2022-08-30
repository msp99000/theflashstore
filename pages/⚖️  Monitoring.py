from styles import *
from backend import *


streamlit_style()

if st.session_state['validated'] == True:
    st.subheader("Realtime Monitoring of the Items")
    st.dataframe(monitoring())

    button = st.button("Email Seller")

    if button:
        st.success("Email sent to Seller")

else:
    st.title("Kindly Log In!!")
