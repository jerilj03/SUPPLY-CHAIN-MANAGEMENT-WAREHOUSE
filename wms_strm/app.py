import streamlit as st
from request import request
from read import read, readsm, readwk
# from store import store
from locate import locate
from database import validate,signup
from receipt import receipt
from add import add
from order import order
import mysql.connector




def main():
    st.set_page_config(layout="wide")
    st.title("WMS")
    # privilege = ""
    placeholder = st.empty()
    if "page" not in st.session_state:
        st.session_state.page = 0
    if st.session_state.page == 0:
        with placeholder.container():
            st.header("User Authentication")
            login_username = st.text_input("Username")
            login_password = st.text_input("Password", type="password")
            # priv = [ "Warehouse Manager","Store Manager", "Warehouse Worker"]
            sel_placeholder = st.empty()
            login_button_placeholder = st.empty()
            
            privilege = sel_placeholder.selectbox("Sign in as",[ "Warehouse Manager","Store Manager", "Warehouse Worker"])
            
            if login_button_placeholder.button('Log in'):
                if validate(login_username, login_password, privilege):
                    # st.session_state.page = 1
                    
                    st.session_state.authenticated_user = True
                    if privilege == "Warehouse Manager":
                        st.session_state.page = 1
                        # p = 1
                    elif privilege == "Store Manager":
                        st.session_state.page = 2
                        # p = 2
                    else:
                        st.session_state.page = 3
                        # p = 3
                    login_button_placeholder.empty()
                    sel_placeholder.empty()
                    
                else:
                    st.error("Invalid username or password.")
    if "authenticated_user" not in st.session_state:
        st.session_state.authenticated_user = False

    if not st.session_state.authenticated_user:
        st.header("User Signup")
        signup_username = st.text_input("New Username")
        signup_password = st.text_input("New Password", type="password")
        priv = [ "Warehouse Manager","Store Manager", "Warehouse Worker"]
        privilege = st.selectbox("Sign up as",priv)
        if st.button("Sign Up"):
            if signup_username is None or signup_password is None or signup_username == "" or signup_password == "":
                st.error("Invalid username or password. Please fill in all the fields.")
            else:
                try:
                    if validate(signup_username, signup_password, privilege):
                        st.error("User already exists")
                    else:
                        signup(signup_username, signup_password, privilege)
                        st.success("User signed up successfully.")
                except mysql.connector.errors.IntegrityError as e:
                    # st.error(f"Error: {str(e)}. This username already exists. Please choose a different username.")
                    st.error("This username already exists")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

    if st.session_state.authenticated_user:
        # if st.session_state.page == 1 and privilege == "Warehouse Manager":
        if st.session_state.page == 1:
            with placeholder.container():    
                #menu = ["Add", "View","Join","Update", "Delete","Average Points","Execute Command"]
                menu = ["View","Locate","Order Item","Add Item","Receipts"]
                choice = st.sidebar.selectbox("Menu", menu)
                # if choice == "Add":
                #     st.subheader("Add Details")
                #     store()
                if choice=="View":
                    st.subheader("View")
                    read()
                elif choice=="Locate":
                    st.subheader("Locate")
                    locate()
                elif choice=="Order Item":
                    st.subheader("Order an item")
                    order()
                elif choice=="Add Item":
                    st.subheader("Add an item")
                    add()
                else:
                    st.subheader("Receipts")
                    receipt()
        if st.session_state.page == 2:
            with placeholder.container():    
                #menu = ["Add", "View","Join","Update", "Delete","Average Points","Execute Command"]
                menu = ["View","Request"]
                choice = st.sidebar.selectbox("Menu", menu)
                if choice=="View":
                    st.subheader("View")
                    readsm()
                elif choice == "Request":
                    st.subheader("Request items")
                    request()
        # if st.session_state.page == 1 and privilege == "Warehouse Worker":
        if st.session_state.page == 3:
            with placeholder.container():    
                #menu = ["Add", "View","Join","Update", "Delete","Average Points","Execute Command"]
                menu = ["View","Locate"]
                choice = st.sidebar.selectbox("Menu", menu)
                if choice=="View":
                    st.subheader("Items")
                    readwk()
                elif choice=="Locate":
                    st.subheader("Locate")
                    locate()
                else:
                    pass
                # elif choice == "Update":
                #     st.subheader("Update Details")
                #     update()
                # elif choice == "Delete":
                #     st.subheader("Delete Details")
                #     delete()
                # elif choice == "Join":
                #     st.subheader("Join Tables")
                #     join()
                # elif choice=="Average Points":
                #     st.subheader("Average Driver Points")
                #     average()
                # elif choice=="Leaderboard History":
                #     st.subheader("Leaderboard History")
                #     history()
                # else:
                #     st.subheader("Execute Queries")
                #     execute()
if __name__ == '__main__':
    main()