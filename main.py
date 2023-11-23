import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
from menu import menu
st.set_page_config(layout="wide")

# hashed_passwords = stauth.Hasher(['karthikcs520', 'aaroncs520', 'deepacs520', 'deepikacs520']).generate()
# print(hashed_passwords)

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# credentials – The dictionary of usernames, names, passwords, and emails
cookies = {"expiry_days":30, "key": "cook", "name": "cs520"}
# authenticator = stauth.Authenticate({"emails":['jsmith@gmail.com', 'rbriggs@gmail.com'],
#                                      "names": ['John Smith', 'Rebecca Briggs'],
#                                      "passwords": ['abc', 'def'],
#                                      "usernames": ['jsmith', 'rbriggs']}, key ='something',
#                                     cookie_name='cs520')


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    menu()
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.reset_password(st.session_state["username"], 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)
#
# try:
#     if authenticator.register_user('Register user', preauthorization=False):
#         st.success('User registered successfully')
# except Exception as e:
#     st.error(e)
