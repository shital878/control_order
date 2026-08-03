import streamlit as st
from outlet_onboarding import outlet_onaboard
from masala_master import masala_master
from book_order import order_details
from login import login, create_user




# Session Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None
    # st.session_state.role = None

if "username" not in st.session_state:
    st.session_state.username = None


# ==========================
# SHOW LOGIN PAGE ONLY
# ==========================

if not st.session_state.logged_in:

    login()
 

    # IMPORTANT
    st.stop()


# ==========================
# AFTER LOGIN ONLY
# ==========================

st.sidebar.success(
    f"Welcome {st.session_state.username}"
)

st.sidebar.write(
    f"Role : {st.session_state.role}"
)

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

menu_list = [
    "Outlet Onboard",
    "Product Master",
    "book_order",
    "Records"
]

if st.session_state.role == "admin":
    menu_list.append("User Management")

st.sidebar.title("Product Order System")

menu = st.sidebar.radio(
    "Menu",
    menu_list
)


if menu == "Outlet Onboard":
    outlet_onaboard()

elif menu == "Product Master":
    masala_master()

elif menu == "book_order":
    order_details()

# elif menu == "Records":
#     records()

if menu == "User Management":
    create_user()

