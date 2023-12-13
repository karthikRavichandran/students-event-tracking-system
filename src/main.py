from server.server import Server
from server.authenticator import Authenticator
import streamlit as st

if __name__ == "__main__":
    auth = Authenticator()
    sid = auth.authenticate()
    if st.session_state["authentication_status"]:
        Server(sid.values[0])