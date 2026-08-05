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


       
    
    
    elif menu == "Cart":

        st.title("🛒 Shopping Cart")

        if len(st.session_state.cart) == 0:

            st.info("Cart is Empty.")

        else:

            # st.success(f"Customer : {st.session_state.customer_name}")

            customer = st.session_state.get("customer_name", "")

            st.info(f"Customer : {customer}")

            grand_total = 0

            st.markdown("""
<style>

.cart-header{
    font-weight:bold;
    font-size:18px;
    padding-bottom:8px;
}

.cart-row{
    display:flex;
    align-items:center;
    gap:10px;
    border-bottom:1px solid #ddd;
    padding:10px 0;
}

.product{
    flex:3;
    word-wrap:break-word;
    white-space:normal;
    font-size:15px;
    font-weight:500;
}

.qty{
    flex:1;
}

.rate{
    flex:1;
    text-align:center;
}

.amount{
    flex:1;
    text-align:center;
}

.delete{
    flex:1;
    text-align:center;
}

@media (max-width:768px){

.product{
    flex:2;
    font-size:13px;
}

.rate{
    font-size:12px;
}

.amount{
    font-size:12px;
}

}

</style>
""", unsafe_allow_html=True)

# Header
        h1,h2,h3,h4,h5 = st.columns([3,1,1,1,1])
        
        h1.markdown("**Product**")
        h2.markdown("**Qty**")
        h3.markdown("**Rate**")
        h4.markdown("**Amount**")
        h5.markdown("**Delete**")
        
        remove_index=None
        
        for i,item in enumerate(st.session_state.cart):
        
            amount=item["qty"]*item["rate"]
            grand_total+=amount
        
            c1,c2,c3,c4,c5=st.columns([3,1,1,1,1])
        
            with c1:
            
                st.markdown(
                    f"""
                    <div style="
                    white-space:normal;
                    word-break:break-word;
                    line-height:18px;
                    font-size:15px;
                    ">
                    {item['masala_name']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
            with c2:
            
                item["qty"]=st.number_input(
                    "",
                    min_value=1,
                    max_value=item["stock"],
                    value=item["qty"],
                    key=f"qty_{i}"
                )
        
            with c3:
                st.write(f"₹{item['rate']}")
        
            with c4:
                st.write(f"₹{item['qty']*item['rate']}")
        
            with c5:
            
                if st.button("🗑",key=f"del_{i}"):
                
                    remove_index=i
        
            st.divider()

            # h1,h2,h3,h4,h5 = st.columns([4,1,1,1,1])

            # h1.markdown("**Product**")
            # h2.markdown("**Qty**")
            # h3.markdown("**Rate**")
            # h4.markdown("**Amount**")
            # h5.markdown("**Delete**")

            # remove_index = None

            # for i, item in enumerate(st.session_state.cart):

            #     amount = item["qty"] * item["rate"]
            #     grand_total += amount

            #     with st.container(border=True):
                
            #         # First Row
            #         st.markdown(f"### {item['masala_name']}")

            #         # Second Row
            #         col1, col2, col3, col4 = st.columns([2,2,2,1])

            #         with col1:
            #             new_qty = st.number_input(
            #                 "Qty",
            #                 min_value=1,
            #                 max_value=item["stock"],
            #                 value=item["qty"],
            #                 key=f"cart_qty_{i}"
            #             )
            #             item["qty"] = new_qty

            #         with col2:
            #             st.metric("Rate", f"₹ {item['rate']}")

            #         with col3:
            #             st.metric("Amount", f"₹ {new_qty * item['rate']}")

            #         with col4:
            #             if st.button("🗑", key=f"delete_{i}"):
            #                 remove_index = i


            # for i, item in enumerate(st.session_state.cart):

            #     c1,c2,c3,c4,c5 = st.columns([4,1,1,1,1])

            #     # Product Name
            #     with c1:
            #         st.write(item["masala_name"])

            #     # Qty
            #     with c2:

            #         new_qty = st.number_input(
            #             "",
            #             min_value=1,
            #             max_value=item["stock"],
            #             value=item["qty"],
            #             key=f"cart_qty_{i}"
            #         )

            #         item["qty"] = new_qty

            #     # Rate
            #     with c3:
            #         st.write(f"₹ {item['rate']}")

            #     amount = new_qty * item["rate"]
            #     grand_total += amount

            #     # Amount
            #     with c4:
            #         st.write(f"₹ {amount}")

            #     # Delete
            #     with c5:

            #         if st.button("🗑", key=f"delete_{i}"):

            #             remove_index = i

                # st.divider()

            if remove_index is not None:

                st.session_state.cart.pop(remove_index)

                st.rerun()

            st.markdown("###")
            st.success(f"Grand Total : ₹ {grand_total}")

            col1,col2,col3 = st.columns(3)

            with col1:

                if st.button("⬅ Continue Shopping"):

                    st.session_state.selected_category = None
                    st.rerun()

            with col2:

                if st.button("🗑 Clear Cart"):

                    st.session_state.cart = []
                    st.rerun()

            with col3:

                if st.button("✅ Submit Order", use_container_width=True):
                
                    if len(st.session_state.cart) == 0:
                        st.warning("Cart is Empty.")

                    else:
                    
                        cursor = connection.cursor()

                        error = False

                        # -------- Check Stock First --------
                        for item in st.session_state.cart:
                        
                            cursor.execute("""
                                SELECT inventory_qty
                                FROM masala_master
                                WHERE id=%s
                            """, (item["id"],))

                            stock = cursor.fetchone()[0]

                            if item["qty"] > stock:
                            
                                st.error(
                                    f"{item['masala_name']} has only {stock} Qty available."
                                )

                                error = True

                        # -------- Save Order --------
                        if not error:
                        
                            for item in st.session_state.cart:
                            
                                amount = item["qty"] * item["rate"]

                                # Insert Order
                                cursor.execute("""
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
                                    st.session_state.get("customer_name"),
                                    item["masala_name"],
                                    item["qty"],
                                    item["rate"],
                                    amount
                                ))

                                # Reduce Inventory
                                cursor.execute("""
                                    UPDATE masala_master
                                    SET inventory_qty = inventory_qty - %s
                                    WHERE id = %s
                                """,
                                (
                                    item["qty"],
                                    item["id"]
                                ))

                            connection.commit()

                            st.success("✅ Order Submitted Successfully")

                            # Clear Cart
                            st.session_state.cart = []

                            # Return to Category Page
                            st.session_state.selected_category = None

                            cursor.close()

                            st.rerun()











# order_details()