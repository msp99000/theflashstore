import yaml
from backend import *
from styles import *
from plots import *

streamlit_style()


def sidebar():
    st.sidebar.title(f"Welcome {name}")
    authenticator.logout("Logout", "sidebar")


with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

st.session_state['validated'] = authentication_status

if authentication_status:

    sidebar()
    
    st.markdown("<h1 style='text-align: center; color: #468189;'>Welcome to Flash Store</h1>",
                unsafe_allow_html=True)
    st.subheader(" ")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('store.webp')