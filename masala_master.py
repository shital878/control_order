import streamlit as st
import pandas as pd
import psycopg2
import os
import base64
from db_config import DB_CONFIG


def set_background(image_name):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(BASE_DIR, "images", image_name)

    if os.path.exists(image_path):

        with open(image_path, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()

        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

    else:
        st.error(f"Image not found : {image_path}")




def masala_master():

    # set_background("grey.png")

    st.header("📦 Product Master")

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    os.makedirs("images", exist_ok=True)

    menu = st.sidebar.radio(
        "Master Menu",
        [
            "Category Master",
            "Insert Product",
            "View Product"
        ]
    )

    #################################################
    # CATEGORY MASTER
    #################################################

    if menu == "Category Master":

        set_background("grey.png")

        st.subheader("Create Category")

        category_name = st.text_input(
            "Category Name"
        )

        category_image = st.file_uploader(
            "Category Image",
            type=["png", "jpg", "jpeg"]
        )

        if st.button("Save Category"):

            if category_name.strip() == "":

                st.error(
                    "Category Name Mandatory"
                )

            else:

                cur.execute(
                    """
                    SELECT COUNT(*)
                    FROM category_master
                    WHERE category_name=%s
                    """,
                    (category_name,)
                )

                cnt = cur.fetchone()[0]

                if cnt > 0:

                    st.error(
                        "Category Already Exists"
                    )

                else:

                    image_name = None

                    if category_image:

                        image_name = (
                            category_image.name
                        )

                        with open(
                            os.path.join(
                                "images",
                                image_name
                            ),
                            "wb"
                        ) as f:

                            f.write(
                                category_image.getbuffer()
                            )

                    cur.execute(
                        """
                        INSERT INTO category_master
                        (
                            category_name,
                            category_image
                        )
                        VALUES
                        (
                            %s,
                            %s
                        )
                        """,
                        (
                            category_name,
                            image_name
                        )
                    )

                    conn.commit()

                    st.success(
                        "Category Saved"
                    )

    #################################################
    # INSERT PRODUCT
    #################################################

    elif menu == "Insert Product":

        set_background("light_pink.png")

        category_df = pd.read_sql(
            """
            SELECT
                category_id,
                category_name
            FROM category_master
            ORDER BY category_name
            """,
            conn
        )

        if category_df.empty:

            st.warning(
                "Please create category first."
            )

        else:

            category = st.selectbox(
                "Category",
                category_df[
                    "category_name"
                ].tolist()
            )

            category_id = (
                category_df.loc[
                    category_df[
                        "category_name"
                    ] == category,
                    "category_id"
                ].values[0]
            )

            st.write(
                f"Selected Category ID : {category_id}"
            )

            masala_name = st.text_input(
                "Product Name"
            )

            masala_image = st.file_uploader(
                "Product Image",
                type=[
                    "png",
                    "jpg",
                    "jpeg"
                ]
            )

            inventory_qty = st.number_input(
                "Inventory Qty",
                min_value=0,
                value=0
            )

            rate = st.number_input(
                "Rate",
                min_value=0.0,
                value=0.0,
                step=1.0
            )

            status = st.selectbox(
                "Status",
                [
                    "Active",
                    "Inactive"
                ]
            )

            if st.button(
                "Save Product"
            ):

                if masala_name.strip() == "":

                    st.error(
                        "Product Name Mandatory"
                    )

                else:

                    cur.execute(
                        """
                        SELECT COUNT(*)
                        FROM masala_master
                        WHERE masala_name=%s
                        """,
                        (masala_name,)
                    )

                    cnt = cur.fetchone()[0]

                    if cnt > 0:

                        st.error(
                            "Product Already Exists"
                        )

                    else:

                        product_image = None

                        if masala_image:

                            product_image = (
                                masala_image.name
                            )

                            with open(
                                os.path.join(
                                    "images",
                                    product_image
                                ),
                                "wb"
                            ) as f:

                                f.write(
                                    masala_image.getbuffer()
                                )

                        try:

                            cur.execute(
                                """
                                INSERT INTO
                                masala_master
                                (
                                    category_id,
                                    masala_name,
                                    masala_image,
                                    inventory_qty,
                                    rate,
                                    status
                                )
                                VALUES
                                (
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s
                                )
                                """,
                                (
                                    int(category_id),
                                    masala_name,
                                    product_image,
                                    inventory_qty,
                                    rate,
                                    status
                                )
                            )

                            conn.commit()

                            st.success(
                                "Product Saved Successfully"
                            )

                        except Exception as e:

                            st.error(e)

    #################################################
    # VIEW PRODUCTS
    #################################################

    elif menu == "View Product":

        set_background("pink.png")
    
        query = """
        SELECT
            m.id,
            c.category_name,
            m.masala_name,
            m.inventory_qty,
            m.rate,
            m.status,
            m.created_at,
            c.category_image,
            m.masala_image
        FROM masala_master m
        JOIN category_master c
        ON m.category_id = c.category_id
        ORDER BY m.id DESC
        """
    
        df = pd.read_sql(query, conn)
    
        # ==========================
        # SEARCH BOX
        # ==========================
    
        search_text = st.text_input(
            "🔍 Search Product / Category",
            placeholder="Enter Product Name or Category"
        )
    
        if search_text:
        
            df = df[
                df["masala_name"]
                .str.contains(search_text,
                              case=False,
                              na=False)
                |
                df["category_name"]
                .str.contains(search_text,
                              case=False,
                              na=False)
            ]
    
        st.dataframe(
            df.drop(
                columns=[
                    "category_image",
                    "masala_image"
                ]
            ),
            use_container_width=True,
            hide_index=True
        )
    
        st.write("")
    
        for i, row in df.iterrows():
        
            with st.container(border=True):
            
                c1, c2, c3 = st.columns([1,1,3])
    
                with c1:
                
                    if row["category_image"]:
                    
                        path = os.path.join(
                            "images",
                            row["category_image"]
                        )
    
                        if os.path.exists(path):
                            st.image(path, width=100)
    
                with c2:
                
                    if row["masala_image"]:
                    
                        path = os.path.join(
                            "images",
                            row["masala_image"]
                        )
    
                        if os.path.exists(path):
                            st.image(path, width=100)
    
                with c3:
                
                    st.markdown(f"""
                    **Category :** {row['category_name']}
    
                    **Product :** {row['masala_name']}
    
                    **Qty :** {row['inventory_qty']}
    
                    **Rate :** ₹ {row['rate']}
    
                    **Status :** {row['status']}
                    """)

    # elif menu == "View Product":

    #     set_background("pink.png")

    #     query = """
    #     SELECT
    #         m.id,
    #         c.category_name,
    #         m.masala_name,
    #         m.inventory_qty,
    #         m.rate,
    #         m.status,
    #         m.created_at,
    #         c.category_image,
    #         m.masala_image
    #     FROM masala_master m
    #     JOIN category_master c
    #     ON m.category_id =
    #        c.category_id
    #     ORDER BY m.id DESC
    #     """

    #     df = pd.read_sql(
    #         query,
    #         conn
    #     )

    #     st.dataframe(
    #         df.drop(
    #             columns=[
    #                 "category_image",
    #                 "masala_image"
    #             ]
    #         ),
    #         use_container_width=True,
    #         hide_index=True
    #     )

    #     st.write("")

    #     for i, row in df.iterrows():

    #         with st.container(border=True):

    #             c1, c2, c3 = st.columns(
    #                 [1, 1, 3]
    #             )

    #             with c1:

    #                 if row[
    #                     "category_image"
    #                 ]:

    #                     path = os.path.join(
    #                         "images",
    #                         row[
    #                             "category_image"
    #                         ]
    #                     )

    #                     if os.path.exists(path):

    #                         st.image(
    #                             path,
    #                             width=100
    #                         )

    #             with c2:

    #                 if row[
    #                     "masala_image"
    #                 ]:

    #                     path = os.path.join(
    #                         "images",
    #                         row[
    #                             "masala_image"
    #                         ]
    #                     )

    #                     if os.path.exists(path):

    #                         st.image(
    #                             path,
    #                             width=100
    #                         )

    #             with c3:

    #                 st.markdown(
    #                     f"""
    #                     **Category :**
    #                     {row['category_name']}

    #                     **Product :**
    #                     {row['masala_name']}

    #                     **Qty :**
    #                     {row['inventory_qty']}

    #                     **Rate :**
    #                     ₹ {row['rate']}

    #                     **Status :**
    #                     {row['status']}
    #                     """
    #                 )

    # cur.close()
    # conn.close()