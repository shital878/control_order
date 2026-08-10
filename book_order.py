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
#     st.markdown("""
# <style>

# /* Main Background */

# [data-testid="stAppViewContainer"]{
# background: linear-gradient(to right,#d6eaf8,#f9ebea);
# }

# /* Center Title */

# .main-title{
# font-size:40px;
# font-weight:bold;
# text-align:center;
# color:#154360;
# margin-bottom:25px;
# }

# /* Card Design */

# .card{
# background:white;
# padding:30px;
# border-radius:12px;
# box-shadow:0px 4px 12px rgba(0,0,0,0.15);
# margin-bottom:20px;
# }

# /* Text Input */

# div[data-baseweb="input"] > div{
# background-color:#fdfefe;
# border:2px solid #2E86C1;
# border-radius:8px;
# }

# div[data-baseweb="input"] > div:focus-within{
# border:2px solid #1B4F72;
# background-color:#EBF5FB;
# }

# /* Labels */

# label{
# color:#154360 !important;
# font-weight:600;
# }

#  /* Buttons */

# .stButton > button,
# div[data-testid="stFormSubmitButton"] > button{
# background:#28B463;
# color:white;
# border-radius:8px;
# height:42px;
# width:200px;
# font-weight:bold;
# border:none;
# }

# /* Hover */

# .stButton > button:hover,
# div[data-testid="stFormSubmitButton"] > button:hover{
# background:#1D8348;
# color:white;
# }

# /* Sidebar */

# section[data-testid="stSidebar"]{
# background-color:#F8C471;
# }

# </style>
# """, unsafe_allow_html=True)


    st.markdown("""
    <style>
    
    /* ==========================================
       MAIN BACKGROUND
       ========================================== */
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(
            to right,
            #d6eaf8,
            #f9ebea
        );
    }
    
    
    /* ==========================================
       CENTER TITLE
       ========================================== */
    
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #154360;
        margin-bottom: 25px;
    }
    
    
    /* ==========================================
       CARD DESIGN
       ========================================== */
    
    .card {
        background: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }
    
    
    /* ==========================================
       TEXT INPUT
       ========================================== */
    
    div[data-baseweb="input"] > div {
        background-color: #fdfefe;
        border: 2px solid #2E86C1;
        border-radius: 8px;
    }
    
    div[data-baseweb="input"] > div:focus-within {
        border: 2px solid #1B4F72;
        background-color: #EBF5FB;
    }
    
    
    /* ==========================================
       LABELS
       ========================================== */
    
    label {
        color: #154360 !important;
        font-weight: 600;
    }
    
    
    /* ==========================================
       BUTTONS
       ========================================== */
    
    .stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background: #28B463;
        color: white;
        border-radius: 8px;
        height: 42px;
        width: 200px;
        font-weight: bold;
        border: none;
    }
    
    
    /* ==========================================
       BUTTON HOVER
       ========================================== */
    
    .stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background: #1D8348;
        color: white;
    }
    
    
    /* ==========================================
       SIDEBAR
       ========================================== */
    
    section[data-testid="stSidebar"] {
        background-color: #F8C471;
    }
    
    
    /* ==========================================
       MOBILE RESPONSIVE DESIGN
       ========================================== */
    
    @media (max-width: 768px) {
    
        /* Page spacing */
        .block-container {
            padding-left: 10px !important;
            padding-right: 10px !important;
            padding-top: 15px !important;
        }
    
        /* Main title */
        .main-title {
            font-size: 28px !important;
            margin-bottom: 15px !important;
        }
    
        /* Headings */
        h1 {
            font-size: 28px !important;
        }
    
        h2 {
            font-size: 23px !important;
        }
    
        h3 {
            font-size: 20px !important;
        }
    
        /* ======================================
           KEEP CART COLUMNS HORIZONTAL
           ====================================== */
    
        div[data-testid="stHorizontalBlock"] {
            flex-wrap: nowrap !important;
            gap: 8px !important;
            align-items: center !important;
        }
    
        div[data-testid="column"] {
            min-width: 0 !important;
            padding: 0 !important;
        }
    
        /* ======================================
           NUMBER INPUT
           ====================================== */
    
        div[data-testid="stNumberInput"] {
            width: 100% !important;
        }
    
        div[data-testid="stNumberInput"] input {
            font-size: 14px !important;
            padding-left: 5px !important;
            padding-right: 5px !important;
        }
    
        /* ======================================
           CART TEXT
           ====================================== */
    
        div[data-testid="column"] p {
            font-size: 13px !important;
            word-break: break-word !important;
        }
    
        /* ======================================
           BUTTONS
           ====================================== */
    
        .stButton > button {
            width: 100% !important;
            min-width: 0 !important;
            font-size: 12px !important;
            padding: 5px !important;
            white-space: nowrap !important;
        }
    
        /* ======================================
           CUSTOMER MESSAGE
           ====================================== */
    
        div[data-testid="stAlert"] {
            font-size: 14px !important;
        }
    
    }
    
    </style>
    """, unsafe_allow_html=True)
    


    # ---------------- TITLE ----------------
    st.markdown('<div class="main-title">Outlet Management System</div>', unsafe_allow_html=True)


    st.header("Order Master")

    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    menu = st.sidebar.radio("Order", ["Order","Update","Delivery","Bill","Cart"])


    # ---------------- SESSION ----------------

    if "cart" not in st.session_state:
        st.session_state.cart = []
    
    if "customer_name" not in st.session_state:
        st.session_state.customer_name = ""
    
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None



    # # ---------------- Session ----------------
    # if "cart" not in st.session_state:
    #     st.session_state.cart = []
    
    # if "selected_category" not in st.session_state:
    #     st.session_state.selected_category = None
    
    # if "customer_name" not in st.session_state:
    #     st.session_state.customer_name = ""
    
    # # ---------------- Cart Count ----------------
    # cart_count = len(st.session_state.cart)
    
    # # ---------------- Sidebar Menu ----------------
    # menu = st.sidebar.radio(
    #     "Order",
    #     (
    #         "Order",
    #         "Update",
    #         "Delivery",
    #         "Bill",
    #         "cart"
    #     )
    # )

    query = "SELECT * FROM masala_master"
    df = pd.read_sql(query, connection)

    # Load Customer Master
    cust_query = "SELECT shop_name FROM customer"
    cust_df = pd.read_sql(cust_query, connection)





# ================= ORDER PAGE =================

    # if menu == "Order":
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
    
            # cust_name = st.selectbox(
            #     "Select Customer",
            #     cust_df["shop_name"]
            # )

            cust_name = st.selectbox(
    "Select Customer",
    cust_df["shop_name"],
    key="customer_select"
)

# Save customer in session
            st.session_state.customer_name = cust_name
            




            if "selected_category" not in st.session_state:
                st.session_state.selected_category = None

            if st.session_state.selected_category is None:
            
                cursor.execute("""
                SELECT
                    category_id,
                    category_name,
                    category_image
                FROM category_master
                ORDER BY category_name
                """)

                category_df = pd.DataFrame(
                    cursor.fetchall(),
                    columns=[
                        "category_id",
                        "category_name",
                        "category_image"
                    ]
                )

                cols = st.columns(3)

                for i, row in category_df.iterrows():
                
                    col = cols[i % 3]

                    image_path = os.path.join(
                        "images",
                        row["category_image"]
                    )

                    with col:
                    
                        st.image(image_path, width=120)

                        if st.button(
                            row["category_name"],
                            key=row["category_id"]
                        ):

                            st.session_state.selected_category = row["category_id"]

                            st.rerun()


            else:
            
                category_id = st.session_state.selected_category

                if st.button("⬅ Back"):
                
                    st.session_state.selected_category = None

                    st.rerun()

                cursor.execute("""
                SELECT
                    id,
                    masala_name,
                    rate,
                    inventory_qty,
                    masala_image
                FROM masala_master
                WHERE category_id=%s
                ORDER BY masala_name
                """,(category_id,))

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

                for _, row in df.iterrows():
                
                    c1,c2,c3 = st.columns([1,3,1])

                    with c1:
                    
                        st.image(
                            os.path.join(
                                "images",
                                row["masala_image"]
                            ),
                            width=90
                        )

                    with c2:
                    
                        st.write("###",row["masala_name"])
                        st.write("₹",row["rate"])
                        st.write("Stock :",row["inventory_qty"])

            # with c3:

            #     qty = st.number_input(
            #         "",
            #         min_value=0,
            #         key=f"qty_{row['id']}"
            #     )

        # *********************************************************************
            # if "cart" not in st.session_state:
            #     st.session_state.cart = []


            # with c3:

            #     qty = st.number_input(
            #         "Qty",
            #         min_value=0,
            #         step=1,
            #         key=f"qty_{row['id']}"
            #     )

            #     if st.button("Add", key=f"add_{row['id']}"):
                
            #         if qty > 0:
                    
            #             # Prevent duplicate product in cart
            #             found = False

            #             for item in st.session_state.cart:
                        
            #                 if item["id"] == row["id"]:
            #                     item["qty"] += qty
            #                     found = True
            #                     break
                            
            #             if not found:
                        
            #                 st.session_state.cart.append({
                            
            #                     "id": row["id"],
            #                     "masala_name": row["masala_name"],
            #                     "qty": qty,
            #                     "rate": row["rate"],
            #                     "stock": row["inventory_qty"]

            #                 })

            #             st.success(f"{row['masala_name']} added to cart")
# ************************************************************************************************
                    with c3:
                    
                        stock = int(row["inventory_qty"])

                        # Show stock
                        st.write(f"Stock : {stock}")

                        if stock <= 0:
                        
                            st.error("Out of Stock")

                        else:
                        
                            qty = st.number_input(
                                "Qty",
                                min_value=0,
                                max_value=stock,      # Cannot order more than available stock
                                step=1,
                                key=f"qty_{row['id']}"
                            )

                            if st.button("Add", key=f"add_{row['id']}"):
                            
                                if qty == 0:
                                    st.warning("Please enter quantity greater than 0.")

                                else:
                                
                                    found = False

                                    for item in st.session_state.cart:
                                    
                                        if item["id"] == row["id"]:
                                        
                                            # Prevent exceeding stock
                                            if item["qty"] + qty > stock:
                                                st.error(f"Only {stock} items available.")
                                            else:
                                                item["qty"] += qty
                                                st.success(f"{row['masala_name']} quantity updated.")

                                            found = True
                                            break
                                        
                                    if not found:
                                    
                                        # st.session_state.cart.append({
                                        #     "id": row["id"],
                                        #     "masala_name": row["masala_name"],
                                        #     "qty": qty,
                                        #     "rate": row["rate"],
                                        #     "stock": stock
                                        # })

                                        st.session_state.customer_name = cust_name

                                        st.session_state.cart.append({
                                            "id": row["id"],
                                            "masala_name": row["masala_name"],
                                            "qty": qty,
                                            "rate": row["rate"],
                                            "stock": stock
                                        })

                                        st.success(f"{row['masala_name']} added to cart.")


       # ==========================================
# SHOPPING CART
# ==========================================

    elif menu == "Cart":

        st.title("🛒 Shopping Cart")

        # ==========================================
        # CHECK CART
        # ==========================================

        if len(st.session_state.cart) == 0:

            st.info("Cart is Empty.")

        else:

            # ==========================================
            # CUSTOMER
            # ==========================================

            customer = st.session_state.get(
                "customer_name",
                ""
            )

            st.info(
                f"Customer : {customer}"
            )

            # ==========================================
            # GRAND TOTAL
            # ==========================================

            grand_total = 0

            # Store index of item to remove
            remove_index = None

            # ==========================================
            # CART ITEMS
            # ==========================================

            for i, item in enumerate(
                st.session_state.cart
            ):

                # ======================================
                # PRODUCT CARD
                # ======================================

                with st.container(border=True):

                    # ----------------------------------
                    # PRODUCT NAME
                    # ----------------------------------

                    st.markdown(
                        f"""
                        <div style="
                            font-size:17px;
                            font-weight:600;
                            word-break:break-word;
                            line-height:22px;
                            margin-bottom:10px;
                        ">
                            🛍️ {item['masala_name']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    # ==================================
                    # QTY / RATE / AMOUNT
                    # ==================================

                    c1, c2, c3 = st.columns(
                        [1, 1, 1]
                    )

                    # ----------------------------------
                    # QUANTITY
                    # ----------------------------------

                    with c1:

                        new_qty = st.number_input(
                            "Qty",
                            min_value=0,
                            max_value=int(
                                item["stock"]
                            ),
                            value=int(
                                item["qty"]
                            ),
                            step=1,
                            key=f"cart_qty_{i}"
                        )

                    # ----------------------------------
                    # RATE
                    # ----------------------------------

                    with c2:

                        st.markdown(
                            "**Rate**"
                        )

                        st.write(
                            f"₹ {item['rate']}"
                        )

                    # ----------------------------------
                    # AMOUNT
                    # ----------------------------------

                    with c3:

                        st.markdown(
                            "**Amount**"
                        )

                        current_amount = (
                            new_qty *
                            item["rate"]
                        )

                        st.write(
                            f"₹ {current_amount}"
                        )

                    # ==================================
                    # UPDATE CART QUANTITY
                    # ==================================

                    if new_qty == 0:

                        remove_index = i

                    else:

                        item["qty"] = new_qty

                        grand_total += (
                            new_qty *
                            item["rate"]
                        )

            # ==========================================
            # REMOVE ITEM IF QTY = 0
            # ==========================================

            if remove_index is not None:

                st.session_state.cart.pop(
                    remove_index
                )

                st.rerun()

            # ==========================================
            # GRAND TOTAL
            # ==========================================

            st.divider()

            st.success(
                f"Grand Total : ₹ {grand_total}"
            )

            st.markdown("###")

            # ==========================================
            # CART ACTION BUTTONS
            # ==========================================

            col1, col2, col3 = st.columns(3)

            # ==========================================
            # CONTINUE SHOPPING
            # ==========================================

            with col1:

                if st.button(
                    "⬅ Continue Shopping",
                    use_container_width=True
                ):

                    st.session_state.selected_category = None

                    st.rerun()

            # ==========================================
            # CLEAR CART
            # ==========================================

            with col2:

                if st.button(
                    "🗑 Clear Cart",
                    use_container_width=True
                ):

                    st.session_state.cart = []

                    st.rerun()

            # ==========================================
            # SUBMIT ORDER
            # ==========================================

            with col3:

                if st.button(
                    "✅ Submit Order",
                    use_container_width=True
                ):

                    # ==================================
                    # CUSTOMER CHECK
                    # ==================================

                    customer_name = st.session_state.get(
                        "customer_name",
                        ""
                    )

                    if not customer_name:

                        st.warning(
                            "Please select customer first."
                        )

                    elif len(
                        st.session_state.cart
                    ) == 0:

                        st.warning(
                            "Cart is Empty."
                        )

                    else:

                        cursor = connection.cursor()

                        error = False

                        # ==================================
                        # CHECK STOCK FIRST
                        # ==================================

                        for item in st.session_state.cart:

                            cursor.execute(
                                """
                                SELECT inventory_qty
                                FROM masala_master
                                WHERE id = %s
                                """,
                                (
                                    item["id"],
                                )
                            )

                            result = cursor.fetchone()

                            # Product does not exist
                            if result is None:

                                st.error(
                                    f"{item['masala_name']} "
                                    f"not found in Product Master."
                                )

                                error = True

                                continue

                            stock = result[0]

                            # Store latest stock
                            item["stock"] = stock

                            # Check quantity
                            if item["qty"] > stock:

                                st.error(
                                    f"{item['masala_name']} "
                                    f"has only {stock} Qty available."
                                )

                                error = True

                        # ==================================
                        # SAVE ORDER
                        # ==================================

                        if not error:

                            try:

                                for item in st.session_state.cart:

                                    amount = (
                                        item["qty"]
                                        *
                                        item["rate"]
                                    )

                                    # ==================================
                                    # DUPLICATE ORDER CHECK
                                    # ==================================

                                    cursor.execute(
                                        """
                                        SELECT COUNT(*)
                                        FROM masala_order
                                        WHERE cust_name = %s
                                        AND masala_name = %s
                                        AND business_date = CURRENT_DATE
                                        """,
                                        (
                                            customer_name,
                                            item["masala_name"]
                                        )
                                    )

                                    count = cursor.fetchone()[0]

                                    if count > 0:

                                        st.warning(
                                            f"{item['masala_name']} "
                                            f"already ordered today."
                                        )

                                        continue

                                    # ==================================
                                    # INSERT ORDER
                                    # ==================================

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
                                            item["id"],
                                            customer_name,
                                            item["masala_name"],
                                            item["qty"],
                                            item["rate"],
                                            amount
                                        )
                                    )

                                    # ==================================
                                    # REDUCE INVENTORY
                                    # ==================================

                                    cursor.execute(
                                        """
                                        UPDATE masala_master
                                        SET inventory_qty =
                                            inventory_qty - %s
                                        WHERE id = %s
                                        """,
                                        (
                                            item["qty"],
                                            item["id"]
                                        )
                                    )

                                # ==================================
                                # COMMIT
                                # ==================================

                                connection.commit()

                                st.success(
                                    "✅ Order Submitted Successfully"
                                )

                                # ==================================
                                # CLEAR CART
                                # ==================================

                                st.session_state.cart = []

                                # ==================================
                                # RETURN TO CATEGORY
                                # ==================================

                                st.session_state.selected_category = None

                                cursor.close()

                                st.rerun()

                            except Exception as e:

                                # ==================================
                                # ROLLBACK IF ERROR
                                # ==================================

                                connection.rollback()

                                st.error(
                                    f"Order submission failed: {e}"
                                )

                                cursor.close()


# order_details()