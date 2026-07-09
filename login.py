import streamlit as st
import psycopg2
import os
import base64
from db_config import DB_CONFIG

st.markdown("""
<style>

/* Main Container */
.custom-box{
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);
    padding:35px;
    border-radius:20px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.25);
}

/* Heading */
.heading{
    font-size:48px;
    font-weight:bold;
    color:darkblue;
}

/* Labels */
label{
    font-size:28px !important;
    font-weight:bold !important;
    color:black !important;
}
            
            /* Selectbox label */
.stSelectbox label p {
    font-weight: bold !important;
    font-size: 16px !important;
    color: black !important;
}
            
            /* Specifically for text input labels */
.stTextInput label p {
    font-weight: bold !important;
    font-size: 16 !important;
    color: black !important;
}
            
#             /* Make all labels bold */
# label {
#     font-weight: bold !important;
#     font-size: 16px !important;
#     color: black !important;
# }

/* Input Text */
.stTextInput input{
    font-size:16px !important;
    font-weight: !important;
    color:black !important;
}

/* Password */
input[type="password"]{
    font-size:16px !important;
    font-weight: !important;
    color:black !important;
}

/* Selectbox text */
div[data-baseweb="select"]{
    font-size:px !important;
    font-weight:bold !important;
}

/* Radio buttons */
div[role="radiogroup"] label{
    font-size:50px !important;
    font-weight:bold !important;
}

/* Button */
.stButton > button{
    background-color:#28a745 !important;
    color:white !important;
    font-size:52px !important;
    font-weight:bold !important;
    height:45px;
    width:150px;
    border-radius:18px;
    border:none;
}

/* Hover */
.stButton > button:hover{
    background-color:#1e7e34 !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# # Get absolute path of current file
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # Image path
# image_path = os.path.join(BASE_DIR, "images", "abc.png")

# # Read image and convert to Base64
# if os.path.exists(image_path):
#     with open(image_path, "rb") as img:
#         encoded = base64.b64encode(img.read()).decode()
# else:
#     st.error(f"Image not found: {image_path}")
#     st.stop()



# st.markdown(f"""
# <style>
# .stApp{{
#     background-image: url("data:image/png;base64,{encoded}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
# }}
# </style>
# """, unsafe_allow_html=True)


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


# st.markdown("""
# <style>
# .stApp {
#     background-color: #F0F8FF;   /* Light Blue */
# }
# </style>
# """, unsafe_allow_html=True)


def login():
    set_background("grey.png")

    st.markdown(
    "<h1 style='text-align:center;color:blue;background-color: yellow;font-weight: bold;padding: 10px;border-radius: 20px;'>" 

    "🎯 Order Control Center"
    
    "</h1>",
    unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        
        st.markdown("<h3 style='text-align:center;color:orange;background-color:skyblue;padding:8px;border-radius:10px'> 📋 User Authentication </h3>",unsafe_allow_html=True)

    st.write("")

    with st.container(border=True):
        username = st.text_input("👤 UserName",placeholder="Enter username")
        password = st.text_input(
                "🔑 Password",
                type="password",
                placeholder="Enter password"
            )
        if st.button(
                "Login",
                use_container_width=True,
                type="primary"
        ):
        
            try:
                    conn = psycopg2.connect(**DB_CONFIG)
                    # The ** operator unpacks the dictionary into keyword arguments:
                    cur = conn.cursor()

                    cur.execute(
                        """
                        SELECT
                            id,
                            username,
                            password_hash,
                            role
                        FROM users_list
                        WHERE username=%s
                        """,
                        (username,)
                    )

                    user = cur.fetchone()

                    cur.close()
                    conn.close()

                    if user:

                        if password == user[2]:

                            st.session_state.logged_in = True
                            st.session_state.user_id = user[0]
                            st.session_state.username = user[1]
                            st.session_state.role = user[3]

                            st.rerun()
                            

                        else:
                            st.error("❌ Invalid Password")

                    else:
                        st.warning("⚠️ User Not Found")

            except Exception as e:
                    st.error(f"Error: {e}") 
             


# login()



def create_user():

    st.markdown("""
<h2 style="
text-align:center;
font-size:40px;
font-weight:bold;
color:darkblue;">
👤 Create and View User
</h2>
""", unsafe_allow_html=True)

    set_background("sky1.png")


    menu = st.radio(
        "User Management",
        ["Create User", "View Users"],horizontal=True
    )

    if menu == "Create User":


        # st.subheader("Create User")

        # username = st.text_input("New Username")
        # password = st.text_input("New Password", type="password")

        # role = st.selectbox(
        #     "Role",
        #     ["user", "admin"]
        # )

        with st.container(border=True):
        
                username = st.text_input(
                    "UserName",placeholder="Enter username"
                )

#                 username = st.text_input(
#     "",
#     key="username",
#     label_visibility="collapsed"
# )

                password = st.text_input(
                    "Password",
                    type="password",placeholder="Enter Password"
                )

                role = st.selectbox(
                    "Role",
                    ["user","admin"]
                )

                st.write("")

                if st.button(
                    "✅ Create User"
                ):
                    pass


        # if st.button("Submit"):

                    try:
                        conn = psycopg2.connect(**DB_CONFIG)
                        cur = conn.cursor()

                        cur.execute(
                            """
                            SELECT 1
                            FROM users_list
                            WHERE username = %s
                            """,
                            (username,)
                        )

                        if cur.fetchone():
                            st.error("Username already exists")

                        else:
                        
                            cur.execute(
                                """
                                INSERT INTO users_list
                                (
                                    username,
                                    password_hash,
                                    role
                                )
                                VALUES
                                (
                                    %s,
                                    %s,
                                    %s
                                )
                                """,
                                (username, password, role)
                            )

                            conn.commit()

                            st.success("User Created Successfully")

                        cur.close()
                        conn.close()

                    except Exception as e:
                        st.error(f"Error: {e}")

    elif menu == "View Users":

        try:
            conn = psycopg2.connect(**DB_CONFIG)

            query = """
            SELECT
                id,
                username,
                role,
                created_at as Created,password_hash as Pwd
            FROM users_list
            ORDER BY id
            """

            import pandas as pd

            df = pd.read_sql(query, conn)

            st.subheader("User List")
            st.dataframe(df, use_container_width=True,hide_index=True)

            conn.close()

        except Exception as e:
            st.error(f"Error: {e}")


# create_user()