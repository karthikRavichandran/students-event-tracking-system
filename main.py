import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from controller.menu import menu
st.set_page_config(layout="wide")

# hashed_passwords = stauth.Hasher(['karthikcs520', 'aaroncs520', 'deepacs520', 'deepikacs520']).generate()
# print(hashed_passwords)

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# credentials – The dictionary of usernames, names, passwords, and emails

cookies = {"expiry_days":30, "key": "cook", "name": "cs520"}


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'main')

# Assigning  Calling Session state for authentication
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    # if user give right Username and password, the line called menu()
    menu()
elif st.session_state["authentication_status"] is False:
    # Error Message is displayed in UI if User credentials didn't match.
    st.error('Username/password is incorrect')

elif st.session_state["authentication_status"] is None:
    # This is when session_state of authentication_status is None i.e., when the app starts and
    # no one is logged in
    st.warning('Please enter your username and password')

