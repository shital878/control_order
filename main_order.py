import streamlit as st

from book_order import order_details
from order import order_details

menu = st.sidebar.radio(
    "Menu",
    [
        "Book Order",
        "Order"
    ]
)

if menu == "Book Order":
    order_details()

elif menu == "Order":
    order_details()