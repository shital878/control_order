import streamlit as st
import pandas as pd
# from order import details
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
   CARD
   ========================================== */

.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 15px;
}


/* ==========================================
   INPUT
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
   LABEL
   ========================================== */

label {
    color: #154360 !important;
    font-weight: 600;
}


/* ==========================================
   NORMAL BUTTON
   ========================================== */

.stButton > button {

    background: #28B463;
    color: white;

    border-radius: 8px;

    height: 38px;

    width: auto;

    padding-left: 18px;
    padding-right: 18px;

    font-weight: bold;

    border: none;
}


/* ==========================================
   FORM SUBMIT BUTTON
   ========================================== */

div[data-testid="stFormSubmitButton"] > button {

    background: #28B463;
    color: white;

    border-radius: 8px;

    height: 38px;

    width: 110px;

    padding-left: 10px;
    padding-right: 10px;

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
   MOBILE
   ========================================== */

@media (max-width: 768px) {

    .block-container {

        padding-left: 8px !important;
        padding-right: 8px !important;
        padding-top: 10px !important;

    }


    .main-title {

        font-size: 27px !important;
        margin-bottom: 12px !important;

    }


    h1 {

        font-size: 27px !important;

    }


    h2 {

        font-size: 22px !important;

    }


    h3 {

        font-size: 19px !important;

    }


    /* --------------------------------------
       PRODUCT CARD COLUMNS
       -------------------------------------- */

    div[data-testid="stHorizontalBlock"] {

        gap: 8px !important;

    }


    div[data-testid="column"] {

        padding-left: 3px !important;
        padding-right: 3px !important;

        min-width: 0 !important;

    }


    /* --------------------------------------
       PRODUCT IMAGE
       -------------------------------------- */

    div[data-testid="stImage"] img {

        max-width: 70px !important;
        height: auto !important;

    }


    /* --------------------------------------
       PRODUCT TEXT
       -------------------------------------- */

    div[data-testid="column"] p {

        font-size: 13px !important;

    }


    /* --------------------------------------
       QTY INPUT
       -------------------------------------- */

    div[data-testid="stNumberInput"] {

        width: 100% !important;

    }


    div[data-testid="stNumberInput"] input {

        font-size: 13px !important;

        padding-left: 4px !important;
        padding-right: 4px !important;

    }


    /* --------------------------------------
       ADD BUTTON
       -------------------------------------- */

    div[data-testid="stFormSubmitButton"] > button {

        width: 90px !important;

        height: 35px !important;

        font-size: 12px !important;

        padding: 4px 8px !important;

    }


    /* --------------------------------------
       NORMAL BUTTON
       -------------------------------------- */

    .stButton > button {

        width: auto !important;

        height: 35px !important;

        font-size: 12px !important;

        padding: 4px 12px !important;

    }

}

</style>
""", unsafe_allow_html=True)





    # ---------------- TITLE ----------------
    st.markdown('<div class="main-title">Outlet Management System</div>', unsafe_allow_html=True)


    st.header("Order Master")

    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()

    menu = st.radio("Order", ["Order","Update","Delivery","Bill","Cart"],horizontal=True)

  
    # ---------------- SESSION ----------------

    if "cart" not in st.session_state:
        st.session_state.cart = []
    
    if "customer_name" not in st.session_state:
        st.session_state.customer_name = ""
    
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None



    query = "SELECT * FROM masala_master"
    df = pd.read_sql(query, connection)

    # Load Customer Master
    cust_query = "SELECT shop_name FROM customer"
    cust_df = pd.read_sql(cust_query, connection)





# ================= ORDER PAGE =================


    if menu == "Order":

        cursor = connection.cursor()

        # =========================================================
        # CUSTOMER
        # =========================================================

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

        # Customer selection

        cust_name = st.selectbox(
            "Select Customer",
            cust_df["shop_name"],
            key="customer_select"
        )

        # Save customer in session

        st.session_state.customer_name = cust_name


        # =========================================================
        # INITIALIZE CATEGORY
        # =========================================================

        if "selected_category" not in st.session_state:

            st.session_state.selected_category = None


        # =========================================================
        # INITIALIZE CART
        # =========================================================

        if "cart" not in st.session_state:

            st.session_state.cart = []


        # =========================================================
        # CATEGORY PAGE
        # =========================================================

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


            if category_df.empty:

                st.warning(
                    "No Categories Found."
                )

            else:

                st.subheader("📂 Select Category")

                # 3 columns for category

                cols = st.columns(3)

                for i, row in category_df.iterrows():

                    col = cols[i % 3]

                    with col:

                        # -----------------------------
                        # CATEGORY IMAGE
                        # -----------------------------

                        if row["category_image"]:

                            image_path = os.path.join(
                                "images",
                                row["category_image"]
                            )

                            if os.path.exists(image_path):

                                st.image(
                                    image_path,
                                    width=100
                                )

                        # -----------------------------
                        # CATEGORY BUTTON
                        # -----------------------------

                        if st.button(
                            row["category_name"],
                            key=f"category_{row['category_id']}",
                            use_container_width=True
                        ):

                            st.session_state.selected_category = (
                                row["category_id"]
                            )

                            st.rerun()


        # =========================================================
        # PRODUCT PAGE
        # =========================================================

        else:

            category_id = (
                st.session_state.selected_category
            )


            # =====================================================
            # BACK BUTTON
            # =====================================================

            if st.button(
                "⬅ Back",
                use_container_width=False
            ):

                st.session_state.selected_category = None

                st.rerun()


            # =====================================================
            # GET PRODUCTS
            # =====================================================

            cursor.execute(
                """
                SELECT
                    id,
                    masala_name,
                    rate,
                    inventory_qty,
                    masala_image
                FROM masala_master
                WHERE category_id = %s
                AND status = 'Active'
                ORDER BY masala_name
                """,
                (category_id,)
            )


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


            # =====================================================
            # NO PRODUCTS
            # =====================================================

            if df.empty:

                st.warning(
                    "No products available in this category."
                )

            else:

                st.subheader("🛍️ Products")


                # =================================================
                # PRODUCT LOOP
                # =================================================

                for _, row in df.iterrows():

                    product_id = int(row["id"])
                    product_name = row["masala_name"]
                    rate = float(row["rate"])
                    stock = int(row["inventory_qty"])

                    image_path = None

                    if row["masala_image"]:
                        image_path = os.path.join(
                            "images",
                            row["masala_image"]
                        )

                    # ==========================================
                    # PRODUCT CARD
                    # ==========================================

                    with st.container(border=True):
                    
                        # LEFT = IMAGE + DETAILS
                        # RIGHT = QTY + ADD

                        left, right = st.columns(
                            [1.3, 0.7],
                            gap="small"
                        )

                        # ======================================
                        # LEFT SIDE
                        # IMAGE
                        # PRODUCT NAME
                        # RATE
                        # STOCK
                        # ======================================

                        with left:
                        
                            if (
                                image_path
                                and os.path.exists(image_path)
                            ):

                                st.image(
                                    image_path,
                                    width=70
                                )

                            else:
                            
                                st.write("🛍️")

                            # Product name BELOW image

                            st.markdown(
                                f"""
                                <div style="
                                    font-size:15px;
                                    font-weight:600;
                                    line-height:20px;
                                    word-break:break-word;
                                    margin-top:3px;
                                ">
                                    {product_name}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            # Rate BELOW product name

                            st.markdown(
                                f"""
                                <div style="
                                    font-size:14px;
                                    margin-top:3px;
                                ">
                                    ₹ {rate:.2f}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                            # Stock BELOW rate

                            st.markdown(
                                f"""
                                <div style="
                                    font-size:13px;
                                    color:#555;
                                    margin-top:2px;
                                ">
                                    Stock : {stock}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        # ======================================
                        # RIGHT SIDE
                        # QTY + ADD BUTTON
                        # ======================================

                        with right:
                        
                            if stock <= 0:
                            
                                st.error("Out of Stock")

                            else:
                            
                                # --------------------------------
                                # PRODUCT FORM
                                # --------------------------------

                                with st.form(
                                    key=f"product_form_{product_id}",
                                    clear_on_submit=True
                                ):

                                    qty = st.number_input(
                                        "Qty",
                                        min_value=1,
                                        max_value=stock,
                                        value=1,
                                        step=1,
                                        key=f"qty_{product_id}"
                                    )

                                    add = st.form_submit_button(
                                        "🛒 Add",
                                        use_container_width=False
                                    )

                                    if add:
                                    
                                        # ==========================
                                        # CHECK EXISTING CART ITEM
                                        # ==========================

                                        found = False

                                        for item in st.session_state.cart:
                                        
                                            if item["id"] == product_id:
                                            
                                                if (
                                                    item["qty"] + qty
                                                    > stock
                                                ):

                                                    st.error(
                                                        f"Only {stock} available."
                                                    )

                                                else:
                                                
                                                    item["qty"] += qty

                                                    st.success(
                                                        f"{product_name} quantity updated."
                                                    )

                                                found = True
                                                break
                                            
                                        # ==========================
                                        # ADD NEW ITEM
                                        # ==========================

                                        if not found:
                                        
                                            st.session_state.cart.append(
                                                {
                                                    "id": product_id,
                                                    "masala_name": product_name,
                                                    "qty": qty,
                                                    "rate": rate,
                                                    "stock": stock
                                                }
                                            )

                                            st.success(
                                                f"{product_name} added to cart."
                            )


                    st.divider()

    elif menu == "Update":
    
            st.title("Update Masala Order")
    
            cust_name = st.selectbox("Select Customer", cust_df["shop_name"])
    
            # cust_name = st.text_input("Customer Name")
            masala_name = st.selectbox("Masala Name", df["masala_name"])
    
            col1, col2 = st.columns(2)
    
            new_qty = col1.number_input("New Quantity", min_value=1)
            new_rate = col2.number_input("New Rate", min_value=1)
    
            if st.button("Update Order"):
    
                new_amount = new_qty * new_rate
    
                cursor = connection.cursor()
    
                update_query = """
                UPDATE masala_order
                SET qty = %s,
                    rate = %s,
                    amount = %s
                WHERE cust_name = %s
                AND masala_name = %s
                AND business_date = CURRENT_DATE
                """
    
                cursor.execute(update_query,
                               (new_qty, new_rate, new_amount, cust_name, masala_name))
    
                connection.commit()
    
                st.success("Order Updated Successfully")

    # ******************************delivery****************


    elif menu == "Delivery":

        # ---------------- PAGE TITLE ----------------
        st.subheader("🚚 Delivery Update")

        # ---------------- FETCH PENDING CUSTOMERS ----------------
        pending_cust_query = """
            SELECT DISTINCT cust_name
            FROM masala_order
            WHERE status = 'Pending'
            ORDER BY cust_name
        """

        pending_df = pd.read_sql(pending_cust_query, connection)

        # ---------------- NO DATA CASE ----------------
        if pending_df.empty:
            st.warning("No pending customers found")
            st.stop()

        # ---------------- CUSTOMER SELECTION ----------------
        cust_name = st.selectbox(
            "Select Customer",
            pending_df["cust_name"],
            index=0
        )

        # ---------------- FETCH CUSTOMER ITEMS ----------------
        items_query = """
            SELECT seq, masala_name, qty, rate
            FROM masala_order
            WHERE status = 'Pending'
            AND cust_name = %s
            ORDER BY seq
        """

        items_df = pd.read_sql(items_query, connection, params=(cust_name,))

        # ---------------- NO ITEMS ----------------
        if items_df.empty:
            st.warning("No pending items for selected customer")
            st.stop()

        st.markdown("### 📦 Order Details")

        # ---------------- HEADER ROW ----------------
        h1, h2, h3, h4 = st.columns([3, 1.5, 1.5, 2])
        h1.markdown("**Masala Name**")
        h2.markdown("**Ordered Qty**")
        h3.markdown("**Rate**")
        h4.markdown("**Delivered Qty**")

        # ---------------- STORE DATA ----------------
        delivery_data = []

        # ---------------- LOOP ITEMS ----------------
        for _, row in items_df.iterrows():

            seq = int(row["seq"])
            masala_name = row["masala_name"]
            ordered_qty = int(row["qty"])
            rate = float(row["rate"])

            col1, col2, col3, col4 = st.columns([3, 1.5, 1.5, 2])

            col1.write(masala_name)
            col2.write(ordered_qty)
            col3.write(f"₹ {rate:.2f}")

            # delivered_qty = col4.number_input(
            #     label="",
            #     min_value=0,
            #     max_value=ordered_qty,
            #     value=ordered_qty,
            #     step=1,
            #     key=f"del_qty_{seq}"
            # )

            delivered_qty = col4.number_input(
    "Delivered Qty",
    min_value=0,
    max_value=ordered_qty,
    value=ordered_qty,
    step=1,
    key=f"del_qty_{seq}",
    label_visibility="collapsed"
)

            delivery_data.append({
                "seq": seq,
                "name": masala_name,
                "ordered": ordered_qty,
                "delivered": delivered_qty,
                "rate": rate
            })

        # ---------------- BUTTONS ----------------
        st.markdown("---")
        btn1, btn2 = st.columns(2)

        # ================= UPDATE DELIVERY =================
        with btn1:
            if st.button("✅ Update Delivery", use_container_width=True):

                cursor = connection.cursor()

                for item in delivery_data:

                    seq = item["seq"]
                    masala_name = item["name"]
                    ordered_qty = item["ordered"]
                    delivered_qty = item["delivered"]
                    rate = item["rate"]

                    # -------- VALIDATION --------
                    if delivered_qty < 0:
                        st.error(f"{masala_name}: Invalid quantity")
                        continue

                    if delivered_qty > ordered_qty:
                        st.error(f"{masala_name}: Delivered > Ordered not allowed")
                        continue

                    # -------- STATUS LOGIC --------
                    if delivered_qty == ordered_qty:
                        status = "Delivered"
                    elif delivered_qty == 0:
                        status = "Pending"
                    else:
                        status = "Partial"

                    amount_del = delivered_qty * rate

                    # -------- UPDATE QUERY --------
                    cursor.execute("""
                        UPDATE masala_order
                        SET qty_del = %s,
                            amount_del = %s,
                            business_date_del = CURRENT_DATE,
                            order_time_del = CURRENT_TIMESTAMP,
                            status = %s
                        WHERE seq = %s
                    """, (
                        delivered_qty,
                        amount_del,
                        status,
                        seq
                    ))

                connection.commit()
                cursor.close()

                st.success(f"Delivery updated successfully for {cust_name} ✅")

                                # ===== FETCH UPDATED DATA FROM DB =====

                bill_query = """
                    SELECT
                        masala_name,
                        qty_del,
                        rate
                    FROM masala_order
                    WHERE cust_name = %s
                    AND status IN ('Delivered','Partial')
                    AND business_date_del = CURRENT_DATE
                """
                
                bill_df = pd.read_sql(
                    bill_query,
                    connection,
                    params=(cust_name,)
                )
                
                if bill_df.empty:
                
                    st.warning("No delivered items found for billing")
                
                    st.stop()
                
                # =====================================================
                # ================= PREPARE TABLE DATA =================
                # =====================================================
                
                total = 0
                
                table_data = [[
                    "Masala Name",
                    "Quantity",
                    "Rate",
                    "Amount"
                ]]
                
                for _, row in bill_df.iterrows():
                
                    amount = row["qty_del"] * row["rate"]
                
                    total += amount
                
                    table_data.append([
                        row["masala_name"],
                        int(row["qty_del"]),
                        f"₹ {row['rate']:.2f}",
                        f"₹ {amount:.2f}"
                    ])
                
                # ===== TOTAL ROW =====
                
                table_data.append([
                    "",
                    "",
                    "TOTAL",
                    f"₹ {total:.2f}"
                ])
                
                # =====================================================
                # ================= GENERATE PDF ======================
                # =====================================================
                
                from io import BytesIO
                
                from reportlab.platypus import (
                    SimpleDocTemplate,
                    Table,
                    TableStyle,
                    Paragraph,
                    Spacer
                )
                
                from reportlab.lib import colors
                from reportlab.lib.styles import getSampleStyleSheet
                from reportlab.lib.pagesizes import A4
                from reportlab.lib.units import inch
                
                buffer = BytesIO()
                
                # =====================================================
                # ================= PDF DOCUMENT ======================
                # =====================================================
                
                doc = SimpleDocTemplate(
                    buffer,
                    pagesize=A4,
                    rightMargin=30,
                    leftMargin=30,
                    topMargin=30,
                    bottomMargin=20
                )
                
                elements = []
                
                styles = getSampleStyleSheet()
                
                # =====================================================
                # ================= TITLE =============================
                # =====================================================
                
                title = Paragraph(
                    "<font size=20><b>MASALA DELIVERY BILL</b></font>",
                    styles['Title']
                )
                
                elements.append(title)
                
                elements.append(Spacer(1, 20))
                
                # =====================================================
                # ================= CUSTOMER INFO =====================
                # =====================================================
                
                customer_info = f"""
                <font size=12>
                <b>Customer:</b> {cust_name}<br/>
                <b>Date:</b> {datetime.now().strftime('%d-%m-%Y %H:%M')}
                </font>
                """
                
                elements.append(
                    Paragraph(
                        customer_info,
                        styles['Normal']
                    )
                )
                
                elements.append(Spacer(1, 20))
                
                # =====================================================
                # ================= FULL WIDTH TABLE ==================
                # =====================================================
                
                table = Table(
                
                    table_data,
                
                    colWidths=[
                    
                        3.5 * inch,
                        1.2 * inch,
                        1.2 * inch,
                        1.5 * inch
                    ]
                )
                
                # =====================================================
                # ================= TABLE STYLE =======================
                # =====================================================
                
                table.setStyle(TableStyle([
                
                    # ===== HEADER =====
                
                    ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
                
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                
                    ('FONTSIZE', (0, 0), (-1, 0), 13),
                
                    # ===== BODY =====
                
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                
                    ('FONTSIZE', (0, 1), (-1, -1), 11),
                
                    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
                
                    # ===== TOTAL ROW =====
                
                    ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                
                    ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
                
                    # ===== GRID =====
                
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                
                    # ===== PADDING =====
                
                    ('TOPPADDING', (0, 0), (-1, -1), 10),
                
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
                
                    # ===== ROW BACKGROUND =====
                
                    ('BACKGROUND', (0, 1), (-1, -2), colors.whitesmoke),
                
                ]))
                
                elements.append(table)
                
                elements.append(Spacer(1, 30))
                
                # =====================================================
                # ================= FOOTER ============================
                # =====================================================
                
                footer = Paragraph(
                    "<font size=11><b>Thank You Visit Again</b></font>",
                    styles['Normal']
                )
                
                elements.append(footer)
                
                # =====================================================
                # ================= BUILD PDF =========================
                # =====================================================
                
                doc.build(elements)
                
                buffer.seek(0)
                
                # =====================================================
                # ================= DOWNLOAD BUTTON ===================
                # =====================================================
                
                st.download_button(
                    label="📄 Download Bill PDF",
                    data=buffer,
                    file_name=f"{cust_name}_bill.pdf",
                    mime="application/pdf"
                )


                

        # ================= CANCEL ORDER =================
        with btn2:

            confirm_cancel = st.checkbox("Confirm Cancel Order")

            if st.button("❌ Cancel Order", use_container_width=True):

                if not confirm_cancel:
                    st.warning("Please confirm cancellation first")
                    st.stop()

                cursor = connection.cursor()

                cursor.execute("""
                    UPDATE masala_order
                    SET status = 'Cancelled',
                        qty_del = 0,
                        amount_del = 0,
                        business_date_del = CURRENT_DATE,
                        order_time_del = CURRENT_TIMESTAMP
                    WHERE cust_name = %s
                    AND status = 'Pending'
                """, (cust_name,))

                connection.commit()
                cursor.close()

                st.error(f"Order cancelled for {cust_name} ❌")

       
        # ================= BILL PAGE =================
     
    elif menu == "Bill":
    
         st.subheader("🧾 Generate Customer Bill")
    
         # ================= BILL TYPE =================
    
         bill_type = st.radio(
             "Select Bill Type",
             ["Delivered", "Pending"],
             horizontal=True
         )
    
         # =========================================================
         # ================= DELIVERED BILL ========================
         # =========================================================
    
         if bill_type == "Delivered":
    
             # -------- FETCH CUSTOMERS --------
    
             bill_cust_query = """
                 SELECT DISTINCT cust_name
                 FROM masala_order
                 WHERE status IN ('Delivered','Partial')
                 ORDER BY cust_name
             """
    
             bill_cust_df = pd.read_sql(
                 bill_cust_query,
                 connection
             )
    
             if bill_cust_df.empty:
                 st.warning("No delivered customers found")
                 st.stop()
    
             # -------- SELECT BOXES --------
    
             col1, col2 = st.columns(2)
    
             with col1:
    
                 cust_name = st.selectbox(
                     "Select Customer",
                     bill_cust_df["cust_name"],
                     key="del_customer"
                 )
    
             # -------- FETCH DELIVERY DATES --------
    
             date_query = """
                 SELECT DISTINCT business_date_del
                 FROM masala_order
                 WHERE cust_name = %s
                 AND status IN ('Delivered','Partial')
                 ORDER BY business_date_del DESC
             """
    
             date_df = pd.read_sql(
                 date_query,
                 connection,
                 params=(cust_name,)
             )
    
             if date_df.empty:
                 st.warning("No delivery dates found")
                 st.stop()
    
             with col2:
    
                 selected_date = st.selectbox(
                     "Select Delivery Date",
                     date_df["business_date_del"],
                     key="del_date"
                 )
    
             # -------- FETCH BILL DATA --------
    
             bill_query = """
                 SELECT
                     masala_name,
                     qty_del,
                     rate
                 FROM masala_order
                 WHERE cust_name = %s
                 AND status IN ('Delivered','Partial')
                 AND business_date_del = %s
             """
    
             bill_df = pd.read_sql(
                 bill_query,
                 connection,
                 params=(cust_name, selected_date)
             )
    
             if bill_df.empty:
                 st.warning("No delivered items found")
                 st.stop()
    
             st.markdown("### 📦 Delivered Items")
    
             # -------- DISPLAY TABLE --------
    
             total = 0
             display_data = []
    
             for _, row in bill_df.iterrows():
    
                 amount = row["qty_del"] * row["rate"]
    
                 total += amount
    
                 display_data.append({
                     "Masala": row["masala_name"],
                     "Qty": int(row["qty_del"]),
                     "Rate": f"₹ {row['rate']:.2f}",
                     "Amount": f"₹ {amount:.2f}"
                 })
    
             st.dataframe(
                 display_data,
                 use_container_width=True
             )
    
             st.markdown(f"### 💰 Total: ₹ {total:.2f}")
    
    
                         # -------- GENERATE PDF --------
    
             if st.button("📄 Generate & Download Delivered Bill"):
    
                 from reportlab.platypus import (
                     SimpleDocTemplate,
                     Table,
                     TableStyle,
                     Paragraph,
                     Spacer
                 )
    
                 from reportlab.lib import colors
                 from reportlab.lib.styles import getSampleStyleSheet
                 from reportlab.lib.pagesizes import A4
                 from reportlab.lib.units import inch
                 from io import BytesIO
    
                 buffer = BytesIO()
    
                 # =====================================================
                 # ================= PDF DOCUMENT ======================
                 # =====================================================
    
                 doc = SimpleDocTemplate(
                     buffer,
                     pagesize=A4,
                     rightMargin=30,
                     leftMargin=30,
                     topMargin=30,
                     bottomMargin=20
                 )
    
                 elements = []
    
                 styles = getSampleStyleSheet()
    
                 # =====================================================
                 # ================= TITLE =============================
                 # =====================================================
    
                 title = Paragraph(
                     "<font size=20><b>MASALA DELIVERY BILL</b></font>",
                     styles['Title']
                 )
    
                 elements.append(title)
    
                 elements.append(Spacer(1, 20))
    
                 # =====================================================
                 # ================= CUSTOMER INFO =====================
                 # =====================================================
    
                 customer_info = f"""
                 <font size=12>
                 <b>Customer:</b> {cust_name}<br/>
                 <b>Delivery Date:</b> {selected_date}
                 </font>
                 """
    
                 elements.append(
                     Paragraph(customer_info, styles['Normal'])
                 )
    
                 elements.append(Spacer(1, 20))
    
                 # =====================================================
                 # ================= TABLE DATA ========================
                 # =====================================================
    
                 table_data = []
    
                 # Header Row
                 table_data.append([
                     "Masala Name",
                     "Quantity",
                     "Rate",
                     "Amount"
                 ])
    
                 # Data Rows
                 for row in display_data:
                 
                     table_data.append([
                         row["Masala"],
                         str(row["Qty"]),
                         row["Rate"],
                         row["Amount"]
                     ])
    
                 # Total Row
                 table_data.append([
                     "",
                     "",
                     "TOTAL",
                     f"₹ {total:.2f}"
                 ])
    
                 # =====================================================
                 # ================= FULL PAGE TABLE ===================
                 # =====================================================
    
                 table = Table(
                     table_data,
    
                     # Full Width Columns
                     colWidths=[
                         3.5 * inch,
                         1.2 * inch,
                         1.2 * inch,
                         1.5 * inch
                     ]
                 )
    
                 # =====================================================
                 # ================= TABLE STYLE =======================
                 # =====================================================
    
                 table.setStyle(TableStyle([
                 
                     # Header Background
                     ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
    
                     # Header Text Color
                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    
                     # Header Font
                     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    
                     # Header Font Size
                     ('FONTSIZE', (0, 0), (-1, 0), 13),
    
                     # Body Font
                     ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    
                     # Body Font Size
                     ('FONTSIZE', (0, 1), (-1, -1), 11),
    
                     # Alignment
                     ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    
                     # Total Row Bold
                     ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    
                     # Total Row Background
                     ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
    
                     # Grid
                     ('GRID', (0, 0), (-1, -1), 1, colors.black),
    
                     # Padding
                     ('TOPPADDING', (0, 0), (-1, -1), 10),
                     ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    
                     # Alternate Row Background
                     ('BACKGROUND', (0, 1), (-1, -2), colors.whitesmoke),
    
                 ]))
    
                 elements.append(table)
    
                 elements.append(Spacer(1, 30))
    
                 # =====================================================
                 # ================= FOOTER ============================
                 # =====================================================
    
                 footer = Paragraph(
                     "<font size=11><b>Thank You Visit Again</b></font>",
                     styles['Normal']
                 )
    
                 elements.append(footer)
    
                 # =====================================================
                 # ================= BUILD PDF =========================
                 # =====================================================
    
                 doc.build(elements)
    
                 buffer.seek(0)
    
                 # =====================================================
                 # ================= DOWNLOAD BUTTON ===================
                 # =====================================================
    
                 st.download_button(
                     label="⬇ Download Delivered PDF",
                     data=buffer,
                     file_name=f"{cust_name}_{selected_date}_delivered_bill.pdf",
                     mime="application/pdf"
                 )
    
         # =========================================================
         # ================= PENDING BILL ==========================
         # =========================================================
    
         elif bill_type == "Pending":
    
             # -------- FETCH CUSTOMERS --------
    
             pending_cust_query = """
                 SELECT DISTINCT cust_name
                 FROM masala_order
                 WHERE status = 'Pending'
                 ORDER BY cust_name
             """
    
             pending_cust_df = pd.read_sql(
                 pending_cust_query,
                 connection
             )
    
             if pending_cust_df.empty:
                 st.warning("No pending customers found")
                 st.stop()
    
             # -------- SELECT BOXES --------
    
             col1, col2 = st.columns(2)
    
             with col1:
    
                 cust_name = st.selectbox(
                     "Select Pending Customer",
                     pending_cust_df["cust_name"],
                     key="pending_customer"
                 )
    
             # -------- FETCH PENDING DATES --------
    
             pending_date_query = """
                 SELECT DISTINCT business_date
                 FROM masala_order
                 WHERE cust_name = %s
                 AND status = 'Pending'
                 ORDER BY business_date DESC
             """
    
             pending_date_df = pd.read_sql(
                 pending_date_query,
                 connection,
                 params=(cust_name,)
             )
    
             if pending_date_df.empty:
                 st.warning("No pending dates found")
                 st.stop()
    
             with col2:
    
                 selected_pending_date = st.selectbox(
                     "Select Pending Date",
                     pending_date_df["business_date"],
                     key="pending_date"
                 )
    
             # -------- FETCH PENDING ITEMS --------
    
             pending_bill_query = """
                 SELECT
                     masala_name,
                     qty,
                     rate
                 FROM masala_order
                 WHERE cust_name = %s
                 AND status = 'Pending'
                 AND business_date = %s
             """
    
             pending_bill_df = pd.read_sql(
                 pending_bill_query,
                 connection,
                 params=(
                     cust_name,
                     selected_pending_date
                 )
             )
    
             if pending_bill_df.empty:
                 st.warning("No pending items found")
                 st.stop()
    
             st.markdown("### 📦 Pending Items")
    
             # -------- DISPLAY TABLE --------
    
             pending_total = 0
    
             pending_display_data = []
    
             for _, row in pending_bill_df.iterrows():
    
                 amount = row["qty"] * row["rate"]
    
                 pending_total += amount
    
                 pending_display_data.append({
    
                     "Masala": row["masala_name"],
    
                     "Qty": int(row["qty"]),
    
                     "Rate": f"₹ {row['rate']:.2f}",
    
                     "Amount": f"₹ {amount:.2f}"
                 })
    
             st.dataframe(
                 pending_display_data,
                 use_container_width=True
             )
    
             st.markdown(
                 f"### 💰 Pending Total: ₹ {pending_total:.2f}"
             )
    
             # -------- GENERATE PDF --------
    
             if st.button("📄 Generate & Download Pending Bill"):
             
                 from reportlab.platypus import (
                     SimpleDocTemplate,
                     Table,
                     TableStyle,
                     Paragraph,
                     Spacer
                 )
         
                 from reportlab.lib import colors
                 from reportlab.lib.styles import getSampleStyleSheet
                 from reportlab.lib.pagesizes import A4
                 from reportlab.lib.units import inch
                 from io import BytesIO
         
                 buffer = BytesIO()
         
                 # ===== A4 PAGE WITH MARGINS =====
         
                 doc = SimpleDocTemplate(
                     buffer,
                     pagesize=A4,
                     rightMargin=30,
                     leftMargin=30,
                     topMargin=30,
                     bottomMargin=20
                 )
         
                 elements = []
         
                 styles = getSampleStyleSheet()
         
                 # =====================================================
                 # ================= TITLE =============================
                 # =====================================================
         
                 title = Paragraph(
                     "<font size=20><b>MASALA PENDING BILL</b></font>",
                     styles['Title']
                 )
         
                 elements.append(title)
         
                 elements.append(Spacer(1, 20))
         
                 # =====================================================
                 # ================= CUSTOMER INFO =====================
                 # =====================================================
         
                 customer_info = f"""
                 <font size=12>
                 <b>Customer:</b> {cust_name}<br/>
                 <b>Pending Date:</b> {selected_pending_date}
                 </font>
                 """
         
                 elements.append(
                     Paragraph(customer_info, styles['Normal'])
                 )
         
                 elements.append(Spacer(1, 20))
         
                 # =====================================================
                 # ================= TABLE DATA ========================
                 # =====================================================
         
                 table_data = []
         
                 # Header
                 table_data.append([
                     "Masala Name",
                     "Quantity",
                     "Rate",
                     "Amount"
                 ])
         
                 # Data Rows
                 for row in pending_display_data:
                 
                     table_data.append([
                         row["Masala"],
                         str(row["Qty"]),
                         row["Rate"],
                         row["Amount"]
                     ])
         
                 # Total Row
                 table_data.append([
                     "",
                     "",
                     "TOTAL",
                     f"₹ {pending_total:.2f}"
                 ])
         
                 # =====================================================
                 # ================= FULL WIDTH TABLE ==================
                 # =====================================================
         
                 table = Table(
                     table_data,
         
                     # Full Page Width
                     colWidths=[
                         3.5 * inch,
                         1.2 * inch,
                         1.2 * inch,
                         1.5 * inch
                     ]
                 )
         
                 # =====================================================
                 # ================= TABLE STYLE =======================
                 # =====================================================
         
                 table.setStyle(TableStyle([
                 
                     # Header Background
                     ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
         
                     # Header Text Color
                     ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
         
                     # Header Font
                     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
         
                     # Header Font Size
                     ('FONTSIZE', (0, 0), (-1, 0), 13),
         
                     # Body Font
                     ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
         
                     # Body Font Size
                     ('FONTSIZE', (0, 1), (-1, -1), 11),
         
                     # Alignment
                     ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
         
                     # Total Row Bold
                     ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
         
                     # Total Row Background
                     ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
         
                     # Grid
                     ('GRID', (0, 0), (-1, -1), 1, colors.black),
         
                     # Padding
                     ('TOPPADDING', (0, 0), (-1, -1), 10),
                     ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
         
                     # Alternate Row Colors
                     ('BACKGROUND', (0, 1), (-1, -2), colors.whitesmoke),
         
                 ]))
         
                 elements.append(table)
         
                 elements.append(Spacer(1, 30))
         
                 # =====================================================
                 # ================= FOOTER ============================
                 # =====================================================
         
                 footer = Paragraph(
                     "<font size=11><b>Your product will be delivered soon</b></font>",
                     styles['Normal']
                 )
         
                 elements.append(footer)
         
                 # =====================================================
                 # ================= BUILD PDF =========================
                 # =====================================================
         
                 doc.build(elements)
         
                 buffer.seek(0)
         
                 # =====================================================
                 # ================= DOWNLOAD BUTTON ===================
                 # =====================================================
         
                 st.download_button(
                     label="⬇ Download Pending PDF",
                     data=buffer,
                     file_name=f"{cust_name}_{selected_pending_date}_pending_bill.pdf",
                     mime="application/pdf"
                 )  



    elif menu == "Cart":

        st.title("🛒 Shopping Cart")

        if len(st.session_state.cart) == 0:

            st.info("Cart is Empty.")

        else:

            customer = st.session_state.get(
                "customer_name",
                ""
            )

            st.info(f"Customer : {customer}")

            grand_total = 0
            remove_index = None

            # ==========================================
            # CART ITEMS
            # ==========================================

            for i, item in enumerate(st.session_state.cart):

                with st.container(border=True):

                    # Product name
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

                    # Qty / Rate / Amount
                    c1, c2, c3 = st.columns([1, 1, 1])

                    # Quantity
                    with c1:

                        new_qty = st.number_input(
                            "Qty",
                            min_value=0,
                            max_value=int(item["stock"]),
                            value=int(item["qty"]),
                            step=1,
                            key=f"cart_qty_{i}"
                        )

                    # Rate
                    with c2:

                        st.markdown("**Rate**")

                        st.write(
                            f"₹ {item['rate']:.2f}"
                        )

                    # Amount
                    with c3:

                        current_amount = (
                            new_qty * item["rate"]
                        )

                        st.markdown("**Amount**")

                        st.write(
                            f"₹ {current_amount:.2f}"
                        )

                    # Update quantity
                    if new_qty == 0:

                        remove_index = i

                    else:

                        item["qty"] = new_qty

                        grand_total += (
                            new_qty * item["rate"]
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

            st.success(
                f"Grand Total : ₹ {grand_total:.2f}"
            )

            st.markdown("###")

            # ==========================================
            # BUTTONS
            # ==========================================

            col1, col2, col3 = st.columns(3)

            # Continue Shopping
            with col1:

                if st.button(
                    "⬅ Continue Shopping",
                    use_container_width=True
                ):

                    st.session_state.selected_category = None

                    st.rerun()

            # Clear Cart
            with col2:

                if st.button(
                    "🗑 Clear Cart",
                    use_container_width=True
                ):

                    st.session_state.cart = []

                    st.rerun()

            # Submit Order
            with col3:

                if st.button(
                    "✅ Submit Order",
                    use_container_width=True
                ):

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
                        # CHECK STOCK
                        # ==================================

                        for item in st.session_state.cart:

                            cursor.execute(
                                """
                                SELECT inventory_qty
                                FROM masala_master
                                WHERE id = %s
                                """,
                                (item["id"],)
                            )

                            result = cursor.fetchone()

                            if result is None:

                                st.error(
                                    f"{item['masala_name']} "
                                    f"not found."
                                )

                                error = True
                                continue

                            stock = result[0]

                            item["stock"] = stock

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
                                        * item["rate"]
                                    )

                                    # Duplicate check
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
                                            item["id"],
                                            customer_name,
                                            item["masala_name"],
                                            item["qty"],
                                            item["rate"],
                                            amount
                                        )
                                    )

                                    # Reduce inventory
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

                                connection.commit()

                                st.success(
                                    "✅ Order Submitted Successfully"
                                )

                                st.session_state.cart = []

                                st.session_state.selected_category = None

                                cursor.close()

                                st.rerun()

                            except Exception as e:

                                connection.rollback()

                                st.error(
                                    f"Order submission failed: {e}"
                                )

                                cursor.close()


# order_details()