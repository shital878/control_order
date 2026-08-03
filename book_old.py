import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
from db_config import DB_CONFIG
from PIL import Image
from io import BytesIO
import os



def order_details():

        # ---------------- PAGE CONFIG ----------------
    st.set_page_config(page_title="Outlet Management System", layout="wide")

    # ---------------- CUSTOM CSS ----------------
    st.markdown("""
<style>

/* Main Background */

[data-testid="stAppViewContainer"]{
background: linear-gradient(to right,#d6eaf8,#f9ebea);
}

/* Center Title */

.main-title{
font-size:40px;
font-weight:bold;
text-align:center;
color:#154360;
margin-bottom:25px;
}

/* Card Design */

.card{
background:white;
padding:30px;
border-radius:12px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
margin-bottom:20px;
}

/* Text Input */

div[data-baseweb="input"] > div{
background-color:#fdfefe;
border:2px solid #2E86C1;
border-radius:8px;
}

div[data-baseweb="input"] > div:focus-within{
border:2px solid #1B4F72;
background-color:#EBF5FB;
}

/* Labels */

label{
color:#154360 !important;
font-weight:600;
}

 /* Buttons */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button{
background:#28B463;
color:white;
border-radius:8px;
height:42px;
width:200px;
font-weight:bold;
border:none;
}

/* Hover */

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover{
background:#1D8348;
color:white;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background-color:#F8C471;
}

</style>
""", unsafe_allow_html=True)

    # ---------------- TITLE ----------------
    st.markdown('<div class="main-title">Outlet Management System</div>', unsafe_allow_html=True)


    st.header("Order Master")

    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    menu = st.sidebar.radio("Order", ["Order","Update","Delivery","Bill"])
    query = "SELECT * FROM masala_master"
    df = pd.read_sql(query, connection)

    # Load Customer Master
    cust_query = "SELECT shop_name FROM customer"
    cust_df = pd.read_sql(cust_query, connection)





# ================= ORDER PAGE =================

    if menu == "Order":

        cursor = connection.cursor()

        # ================= CUSTOMER =================

        cursor.execute("""
            SELECT shop_name
            FROM customer
            ORDER BY shop_name
        """)

        cust_df = pd.DataFrame(
            cursor.fetchall(),
            columns=["shop_name"]
        )

        if cust_df.empty:
            st.warning("No Customers Found.")
            st.stop()

        cust_name = st.selectbox(
            "Select Customer",
            cust_df["shop_name"]
        )

        # ================= PRODUCTS =================

        cursor.execute("""
                SELECT category_id, category_name
                FROM category_master
                ORDER BY category_name
                """)

        category_df = pd.DataFrame(
                    cursor.fetchall(),
                    columns=["category_id", "category_name"]
                )

        selected_category = st.selectbox(
                    "📂 Select Category",
                    category_df["category_name"]
                )

        category_id = category_df.loc[
                    category_df["category_name"] == selected_category,
                    "category_id"
                ].values[0]


        cursor.execute("""
            SELECT
                id,
                masala_name,
                rate,
                inventory_qty,
                masala_image
            FROM masala_master
            ORDER BY masala_name
        """)

        df = pd.DataFrame(
            cursor.fetchall(),
            columns=[
                "id",
                "masala_name",
                "rate",
                "inventory_qty",
                "masala_image"
            ]
        )

        if df.empty:
            st.warning("No Products Found.")
            st.stop()

        # ================= SEARCH =================

        search_text = st.text_input(
            "🔍 Search Product"
        )

        if search_text:

            filtered_df = df[
                df["masala_name"].str.contains(
                    search_text,
                    case=False,
                    na=False
                )
            ]

        else:

            filtered_df = df

        st.markdown("---")

        st.subheader("Enter Order Details")

        # ================= FORM =================

        with st.form(
            "order_form",
            clear_on_submit=True
        ):

            h1, h2, h3, h4 = st.columns(
                [1,3,1,1]
            )

            h1.markdown("### Image")
            h2.markdown("### Product")
            h3.markdown("### Qty")
            h4.markdown("### Rate")

            order_items = []

            # ================= PRODUCT LOOP =================

            for index, row in filtered_df.iterrows():

                masala_id = row["id"]
                masala_name = row["masala_name"]
                rate = int(row["rate"])
                inventory = row["inventory_qty"]
                image_name = row["masala_image"]

                c1, c2, c3, c4 = st.columns(
                    [1,3,1,1]
                )

                # ---------- IMAGE ----------

                with c1:

                    if image_name:

                        image_path = os.path.join(
                            "images",
                            image_name
                        )

                        if os.path.exists(image_path):

                            st.image(
                                image_path,
                                width=70
                            )

                        else:

                            st.write("No Image")

                    else:

                        st.write("No Image")

                # ---------- NAME ----------

                with c2:

                    st.markdown(
                        f"**{masala_name}**"
                    )

                    st.caption(
                        f"Available : {inventory}"
                    )

                # ---------- QTY ----------

                with c3:

                    qty = st.number_input(
                        "",
                        min_value=0,
                        step=1,
                        key=f"qty_{masala_id}"
                    )

                # ---------- RATE ----------

                with c4:

                    rate_input = st.number_input(
                        "",
                        min_value=0,
                        value=rate,
                        key=f"rate_{masala_id}"
                    )

                order_items.append({
                    "id": masala_id,
                    "name": masala_name,
                    "qty": qty,
                    "rate": rate_input,
                    "inventory": inventory
                })

            submitted = st.form_submit_button(
                "Submit Order",
                use_container_width=True
            )

            # ================= SUBMIT =================

            if submitted:
                
                   inserted = False
                   error_found = False
                
                   cursor = connection.cursor()
                
                   for item in order_items:
                    
                       masala_id = item["id"]
                       masala_name = item["name"]
                       qty = item["qty"]
                       rate = item["rate"]
                       inventory = item["inventory"]
                
                       # Skip products not selected
                       if qty == 0:
                           continue
                       
                       # Validate rate
                       if rate <= 0:
                           st.error(f"Please enter a valid rate for {masala_name}")
                           error_found = True
                           continue
                       
                       # Inventory check
                       if qty > inventory:
                           st.error(
                               f"{masala_name}: Only {inventory} items available."
                           )
                           error_found = True
                           continue
                       
                       # Duplicate order check
                       cursor.execute(
                           """
                           SELECT COUNT(*)
                           FROM masala_order
                           WHERE cust_name=%s
                             AND masala_name=%s
                             AND business_date=CURRENT_DATE
                           """,
                           (
                               cust_name,
                               masala_name
                           )
                       )
                
                       count = cursor.fetchone()[0]
                
                       if count > 0:
                           st.warning(
                               f"{masala_name} already ordered today."
                           )
                           continue
                       
                       amount = qty * rate
                
                       # Insert order
                       cursor.execute(
                           """
                           INSERT INTO masala_order
                           (
                               id,
                               cust_name,
                               masala_name,
                               qty,
                               rate,
                               amount,
                               business_date,
                               order_time
                           )
                           VALUES
                           (
                               %s,
                               %s,
                               %s,
                               %s,
                               %s,
                               %s,
                               CURRENT_DATE,
                               CURRENT_TIMESTAMP
                           )
                           """,
                           (
                               masala_id,
                               cust_name,
                               masala_name,
                               qty,
                               rate,
                               amount
                           )
                       )
                
                       # Reduce inventory
                       cursor.execute(
                           """
                           UPDATE masala_master
                           SET inventory_qty = inventory_qty - %s
                           WHERE id = %s
                           """,
                           (
                               qty,
                               masala_id
                           )
                       )
                
                       inserted = True
                
                   # Commit transaction only if there were no validation errors
                   if not error_found:
                       connection.commit()
                
                   cursor.close()
                
                   if inserted:
                       st.success("✅ Order submitted successfully.")



order_details()