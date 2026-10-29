
import streamlit as st
import os
import datetime
import time
# 1)-------------------------------------------------------

# st.title("Hi, I am turtle code")
# st.header("Practice streamlit course")
# st.subheader("Hi let us strt to code")
# st.write("New practice session")

# 2)------------------------------markdown-------------------------

# st.markdown("Turtle code")
# st.markdown("##Turtle code")
# st.markdown("**Turtle** code")
# st.markdown("1.First item \n 2.Second Item")
# str = "print('Hello world')"
# st.code(str)
# st.code("hello")
# st.markdown("----")
# st.markdown('[Google](https://www.google.com)')
# table='''
# a,b
# ---,--
# 1,2
# '''
# st.markdown(table)

# json = {"a":"1,2,3","b":"4,5,6"}
# st.json(json)

# 3)----------------------display---------------------------------

# st.title("Display element")

# st.metric(label='Win speed',value='70ms',delta='5.7')

# table =({"col1":[1,2,3],"col2":[4,5,6]})
# st.table(table)
# st.dataframe(table)

# 4)--------------------------images/audio-----------------------------

# st.image("images/a1.png",width=300,caption="My product")

# st.audio("audio/audio.m4a",start_time=1)



# 5)-------------------------------------------------------

# car_types = ['toyota','fiat','ford','BMW']
# car = st.text_input("Type a car")
# button = st.button("check Availability")

# if button == True:
#     have_it = car.lower() in car_types
#     if have_it:
#         st.write('We have that car!')
#     else:
#         st.write("We don't have that car")

# 6)________________________________________________

# file_name = st.text_input("Enter file name")
# st.write(file_name)

# with open("images/blue.png","rb") as file:
#     btn = st.download_button(
#             label="Download image",
#             data=file,
#             file_name=file_name,
#             mime="image/png"
#     )

# 7)________________________________________________
# image_list = ["images/a1.png","images/blue.png"]
# caption_list = ["tree","blue"]
# st.image(image=image_list,width=200,caption=caption_list)

# st.subheader("Go to chatgpt link")
# # st.link_button('[Google](https://www.google.com)')-which is not working-
# st.markdown('[Google](https://www.google.com)')

# 8)-------------------------------------------------------

# image_list = ["images/a1.png","images/blue.png"]
# caption_list = ["tree","blue"]
# # st.image(image=image_list,width=200,caption=caption_list)

# checks = st.columns(2)

# with checks[0]:
#     images = st.checkbox('Do you want to see photos?')
# with checks[1]:
#     codes = st.checkbox('Do you want to see codes?')

# # images = st.checkbox('Do you want to see photos?')
# # codes = st.checkbox('Do you want to see codes?')

# if images:
#     st.image(image=image_list,width=200,caption=caption_list)
# if codes:
#     st.code("print('Hello turtle code')")
  

# 9)-------------------------------------------------------

# toggles = st.columns(2)

# with toggles[0]:
#     toggle_audio = st.toggle('Enable to audio')
# with toggles[1]:
#     toggle_image = st.toggle('Enable to Image')

# # toggle_audio = st.toggle('Enable to audio')
# # toggle_image = st.toggle('Enable to Image')

# if toggle_audio:
#     st.audio("audio/audio.m4a")
# if toggle_image:
#     st.image("images/a1.png",width=200,caption="My product")

# 10)-------------------------------------------------------

# st.header("Choose your course")

# if "visibility" not in st.session_state:
#     st.session_state.disabled = False

# radio_button =  st.radio('Choose your Course',
#                          ["HTML | CSS :rainbow:",
#                             "JavaScript :rainbow:"],
#                             index=None,
#                             key="visibility",
#                             # disabled=False,
#                             disabled=st.session_state.disabled
#                             )
# # --index value defined none of radio button select

# st.session_state.disabled = True
# if radio_button == "HTML | CSS :rainbow:":
#     st.write("You selected HTML | CSS")
#     # st.session_state.disabled = True

# if radio_button == "JavaScript :rainbow:":
#     st.write("You selected JavaScript")
#     # st.session_state.disabled = True

# 11)-------------------------------------------------------

# st.header("Choose your car")

# car_info = [{
#     "car_make":"Porsche",
#     "car_model":"911"
# },
# {
#     "car_make":"Audi",
#     "car_model":"S4"
# }
# ]

# option = st.selectbox("which poto did you like?",
#                       [car_info[0]['car_make'] + " " + car_info[0]['car_model'],
#                       car_info[1]['car_make'] + " " + car_info[1]['car_model']]
#                       )

# if option == car_info[0]['car_make'] + " " + car_info[0]['car_model']:
#     st.image("images/a1.png",width=200,caption="My product")

# if option == car_info[1]['car_make'] + " " + car_info[1]['car_model']:
#     st.image("images/a2.png",width=200,caption="Model :"+str(car_info[0]['car_model']) + "   " +\
#              "Price :5L")


# 12)-------------------------------------------------------

# options = st.multiselect('What are your favorite companies',
#                          ['Tesla','Google','Amazon'],['Tesla'])#Tesla as default select

# for x in options:
#     if x == 'Tesla':
#         st.image("images/a1.png",width=200,caption="My product")

# 13)----------------------size of image---------------------------------
# st.write("Hello")  

# size = st.slider('Set image size',100,400,200)
# st.write('size :',size)
# st.image("images/a1.png",width=size,caption="My product")


# 14)----------------------Loan calculator---------------------------------

# st.header("Loan calculator")

# loan_amount = st.select_slider('Amount',options=[0,10000,20000,30000])
# loan_maturity = st.select_slider('Month',options=[1,2,3,4,5,6,7,8,9,10,11,12])
# value = loan_amount * loan_maturity
# st.write("Interest Rate")
# st.text('%1')

# calcaulation = ((loan_amount/100)*(1/365) * (loan_maturity*30)) + loan_amount

# st.write('Your payback is ',int(calcaulation))

# 15)-------------------------------------------------------

# name = st.text_input("what is your name?")
# surname = st.text_input("What is your surname?")

# button = st.button('Show')

# if button == True:
#     st.write(f'Welcome {name} {surname}')
    
# else:
#     st.warning("Please enter name...")

# 16)-----------------------Maths-------------------------------- 
# first_number = st.number_input('First Number')
# second_number = st.number_input('Second Number')

# buttons = st.columns(4)
# with buttons[0]:
#     button_addition = st.button('Addition (+)')
# with buttons[1]:
#     button_substraction = st.button('Substraction (-)')
# with buttons[2]:
#     button_multiplication = st.button('Multiplication (*)')
# with buttons[3]:
#     button_division = st.button('Division (/)')

# if button_addition:
#     st.write(f'Addition is : {first_number+second_number}')
# if button_substraction:
#     st.write(f'Substraction is : {first_number-second_number}')
# if button_multiplication:
#     st.write(f'Multiplication is : {first_number*second_number}')
# if button_division:
#     st.write(f'Division is : {first_number/second_number}')

# 17)-----------------------char and word--------------------------------

# st.write("No. of charactera and words...")
# list = []
# txt=st.text_area('Enter text',"",placeholder="Write text here!!!",max_chars=100)  
# analyze_button = st.button('Analyze')
# if analyze_button:
#     st.write(txt)
#     text_split = txt.split(sep=" ")
#     for word in text_split:
#         list.append(word)
#     st.write(f'You wrote {len(txt)} characters. You wrote {len(list)} words.')


# 18)-----------------------Find number of days--------------------------------

# st.header("Find number of days")
# name = st.text_input("Enter Name",placeholder='Name Enter here')
# company = st.text_input("Enter Company Name")
# start_date = st.date_input('Enter Joining Date',datetime.date(2019,12,15))
# end_date = st.date_input("Enter Last date",datetime.date(2026,12,24))

# pt1 = str(start_date).split('-')
# pt2 = str(end_date).split('-')

# t1 = datetime.date(year=int(pt1[0]),month=int(pt1[1]),day=int(pt1[2]))
# t2 = datetime.date(year=int(pt2[0]),month=int(pt2[1]),day=int(pt2[2]))

# if st.button('Show'):
#     st.write(f'Hey {name}! you worked in the {company} company for {(t2-t1).days} days.')


# 19)------------------time input -------------------------------------

# st.header("Time input object")

# first_team = st.text_input('First Team')
# second_team = st.text_input('Seocnd Team')

# t = st.time_input('Set an alarm for ',value=None)

# if st.button('Show'):
#     st.write(f'The match between the {first_team} and {second_team} will start at {t}')

# 20)------------------file uploader-------------------------------------

# st.header("File uploader")

# uploaded_images = st.file_uploader("Choose a Image",accept_multiple_files=True)
# uploaded_texts = st.file_uploader("Choose a text" ,accept_multiple_files=True)

# for upload_image in uploaded_images:
#     st.write('Filename:',upload_image.name)
#     st.image(upload_image)

# for uploaded_text in uploaded_texts:
#     bytes_data = uploaded_text.read()
#     st.write("filename: ",uploaded_text.name)
#     st.write(bytes_data)


# 21)------------------Color picker-------------------------------------

# st.subheader("Color Picker")

# color = st.color_picker('Pick A color' ,'#000000')

# st.markdown(f"<span style='color:{color}'> Welcome to Turtle code!</span>",unsafe_allow_html=True)

# st.write('The current color is',color)

# 22)------------------Find age-------------------------------------

# st.header("Find age")

# with st.form("my_form"):
#     name = st.text_input("Name")
#     surname = st.text_input("SurName")
#     age = st.slider("How old are you")
#     start_day = st.date_input("StartingDate")
#     submit = st.form_submit_button("Submit")
#     if submit:
#         st.write(f'Name : {name} SurName: {surname} Age : {age} Starting : {start_day}')

# 23)------------------sidebar-------------------------------------

# st.subheader("sidebar")

# with st.sidebar:
#     add_selectbox = st.selectbox("How would like to be contacte?",("Mobile Phone","Email"))
#     add_input = st.text_input("Info")

#     add_radio = st.radio("Choose shipping Metod",("Standart (5-15 days)","Express (2-5 days)"))

#     send_button = st.button("Send")

#     if send_button:
#         st.sidebar.write("Sidebar is clicked")

#24)------------------columns-link button----------------------------------------------------------------

# st.subheader("columns-link button")

# col1,col2,col3 = st.columns(3)

# with col1:
#     st.header('Javascript')
#     st.image("images/a1.png",caption="My product")
#     st.link_button('Java acript','https://www.w3schools.com/js/')


# with col2:
#     st.header('Python')
#     st.image("images/a1.png",caption="My product")

# with col3:
#     st.header('Java')
#     st.image("images/a1.png",caption="My product")    


#25)------------------tabs----------------------------------------------------------------

# tab1, tab2 ,tab3 = st.tabs(["Football","Baseball","Tennis"])

# with tab1:
#     st.header("Football")
#     st.image("images/a1.png",caption="My product")
#     st.write("I like to play football")

# with tab2:
#     st.header("Baseball")
# with tab3:
#     st.header("Tennis")


#26)------------------Expander----------------------------------------------------------------

# tab1, tab2 ,tab3 = st.tabs(["Python","Javascript","Java"])

# with tab1:
#     st.header("Python")
#     st.image("images/a1.png",caption="My product")
#     st.write("I want to learn python")
#     with st.expander("See explanation"):
#         st.write("I want to learn python for AI")

#27)------------------Container----------------------------------------------------------------

# with st.expander("java"):
#     with st.container(border=True):
#         st.image("images/a1.png",caption="My product")
#         st.write("This is a container")

# with st.container(border=True):
#     st.image("images/a1.png",caption="My product")
#     st.write("This is a container")

#28)------------------timer and empty----------------------------------------------------------------

# time_input = st.text_input("Enter a time")
# button = st.button("Start")
# if button:
#     # st.write(time_input)
#     with st.empty():
#         for second in range(int(time_input)):
#             st.write(f"{second} seconds have passed")
#             time.sleep(1)
#         st.image("images/a1.png",caption="My product")


#29)------------------Multiple pages----------------------------------------------------------------

# st.sidebar.success('Select a page')

# import streamlit as st

# st.set_page_config(
#     page_title="Programming Website",
#     layout="wide"
# )

# st.title("Programming Website")

# # Sidebar pages
# pages = [
#     "Order",
#     "login"
# ]

# selected_page = st.sidebar.selectbox(
#     "Select a page",
#     pages
# )

# # Display selected page
# if selected_page == "Order":
#     st.header("Home Page")
#     st.write("Welcome to my website!")

# elif selected_page == "login":
#     st.header("Python")
#     st.write("Python programming tutorials")

#30)------------------Generate QR code--------------------------------------------------------------

# import streamlit as st
# import qrcode
# from io import BytesIO

# st.set_page_config(page_title="QR Code Generator")

# st.title("QR Code Generator")

# # Get input from user
# text = st.text_input(
#     "Enter text or URL",
#     placeholder="https://www.google.com"
# )

# if st.button("Generate QR Code"):

#     if text.strip():

#         # Generate QR code
#         qr = qrcode.make(text.strip())

#         # Save QR code in memory
#         buffer = BytesIO()
#         qr.save(buffer, format="PNG")
#         qr_bytes = buffer.getvalue()

#         # Display QR code
#         st.image(qr_bytes, caption="Your QR Code", width=250)

#         # Download QR code
#         st.download_button(
#             label="Download QR Code",
#             data=qr_bytes,
#             file_name="my_qr_code.png",
#             mime="image/png"
#         )

#     else:
#         st.warning("Please enter some text or URL.")


#31)------------------Sales Dashboard--------------------------------------------------------------
# 1)

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# st.set_page_config(
#     page_title="Sales Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# st.title("📊 Sales Dashboard")
# st.write("Welcome to your sales analytics dashboard")

# # 1. Sample sales data
# data = {
#     "Date": [
#         "2026-10-01", "2026-10-02", "2026-10-03",
#         "2026-10-04", "2026-10-05", "2026-10-06",
#         "2026-10-07", "2026-10-08"
#     ],
#     "Product": [
#         "Rice", "Oil", "Sugar", "Rice",
#         "Tea", "Oil", "Sugar", "Tea"
#     ],
#     "Category": [
#         "Grocery", "Grocery", "Grocery", "Grocery",
#         "Beverages", "Grocery", "Grocery", "Beverages"
#     ],
#     "Quantity": [10, 5, 8, 15, 6, 7, 12, 9],
#     "Price": [60, 150, 45, 60, 120, 150, 45, 120]
# }

# df = pd.DataFrame(data)
# df["Date"] = pd.to_datetime(df["Date"])
# df["Sales"] = df["Quantity"] * df["Price"]

# # 2. Sidebar filters
# st.sidebar.header("Filters")

# categories = ["All"] + sorted(df["Category"].unique().tolist())

# selected_category = st.sidebar.selectbox(
#     "Select Category",
#     categories
# )

# if selected_category != "All":
#     filtered_df = df[df["Category"] == selected_category]
# else:
#     filtered_df = df.copy()

# # 3. KPI metrics
# total_sales = filtered_df["Sales"].sum()
# total_orders = len(filtered_df)
# total_quantity = filtered_df["Quantity"].sum()
# average_sales = (
#     total_sales / total_orders if total_orders > 0 else 0
# )

# col1, col2, col3, col4 = st.columns(4)

# col1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
# col2.metric("📦 Total Orders", total_orders)
# col3.metric("🛒 Units Sold", total_quantity)
# col4.metric("📈 Avg. Order Value", f"₹{average_sales:,.0f}")

# st.divider()

# # 4. Sales by date
# st.subheader("Daily Sales")

# daily_sales = (
#     filtered_df.groupby("Date", as_index=False)["Sales"]
#     .sum()
# )

# fig1 = px.bar(
#     daily_sales,
#     x="Date",
#     y="Sales",
#     title="Sales by Date",
#     text_auto=True
# )

# st.plotly_chart(fig1, use_container_width=True)

# # 5. Sales by product
# col5, col6 = st.columns(2)

# with col5:
#     st.subheader("Sales by Product")

#     product_sales = (
#         filtered_df.groupby("Product", as_index=False)["Sales"]
#         .sum()
#     )

#     fig2 = px.bar(
#         product_sales,
#         x="Product",
#         y="Sales",
#         color="Product",
#         title="Product Performance"
#     )

#     st.plotly_chart(fig2, use_container_width=True)

# with col6:
#     st.subheader("Sales by Category")

#     category_sales = (
#         filtered_df.groupby("Category", as_index=False)["Sales"]
#         .sum()
#     )

#     fig3 = px.pie(
#         category_sales,
#         names="Category",
#         values="Sales",
#         title="Category Sales Distribution"
#     )

#     st.plotly_chart(fig3, use_container_width=True)

# # 6. Sales data table
# st.subheader("Sales Details")

# st.dataframe(
#     filtered_df,
#     use_container_width=True,
#     hide_index=True
# )



# ____________________________________________________________________________________;

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np


# st.title("Simple Sales Dashboard")

# np.random.seed(42)

# data = {
#     "Month":["January","February","March","April","May","June"],
#     "Sales":np.random.randint(200,500,6),
#     "Cost":np.random.randint(100,300,6)
# }

# df = pd.DataFrame(data)
# st.subheader("Sales Data")
# st.dataframe(df)

# #Bar Chart

# st.subheader("Sales vs Cost Chart")
# fig,ax = plt.subplots()
# ax.bar(df["Month"],df["Sales"],label="Sales",color="skyblue")
# ax.bar(df["Month"],df["Cost"],label="Cost",color="salmon",alpha=0.7)
# ax.legend()

# st.pyplot(fig)


# #Filter option
# st.subheader("Monthly sales Analysis")
# selected_month = st.selectbox("Select a month: ",df["Month"])
# selected_data = df[df["Month"]==selected_month]

# st.write(f"Sales in {selected_month}:{selected_data["Sales"].values[0]}")
# st.write(f"Cost in {selected_month}: {selected_data["Cost"].values[0]}")


# _____________________________Log in page_______________________________________________________;

# import streamlit as st
# import sqlite3
# import hashlib
# import os

# st.set_page_config(
#     page_title="Sales Management System",
#     page_icon="🔐",
#     layout="centered"
# )

# # Create SQLite database and user table
# conn = sqlite3.connect("users.db")
# conn.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         username TEXT PRIMARY KEY,
#         password_hash TEXT NOT NULL,
#         salt TEXT NOT NULL
#     )
# """)
# conn.commit()
# conn.close()


# def hash_password(password, salt):
#     return hashlib.pbkdf2_hmac(
#         "sha256",
#         password.encode(),
#         salt,
#         200000
#     ).hex()


# def register_user(username, password):
#     username = username.strip()

#     if not username or not password:
#         return False, "Enter username and password."

#     salt = os.urandom(16)
#     password_hash = hash_password(password, salt)

#     try:
#         with sqlite3.connect("users.db") as conn:
#             conn.execute(
#                 """INSERT INTO users
#                    (username, password_hash, salt)
#                    VALUES (?, ?, ?)""",
#                 (username, password_hash, salt)
#             )
#         return True, "Registration successful!"

#     except sqlite3.IntegrityError:
#         return False, "Username already exists."


# def verify_user(username, password):
#     with sqlite3.connect("users.db") as conn:
#         user = conn.execute(
#             """SELECT password_hash, salt
#                FROM users WHERE username = ?""",
#             (username.strip(),)
#         ).fetchone()

#     if user is None:
#         return False

#     saved_hash, salt = user
#     entered_hash = hash_password(password, salt)

#     return entered_hash == saved_hash


# # Login interface
# st.title("🔐 Sales Management System")

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if st.session_state.logged_in:
#     st.success(
#         f"Welcome, {st.session_state.username}!"
#     )

#     st.header("Sales Dashboard")
#     st.write("You are logged in successfully.")

#     if st.button("Logout"):
#         st.session_state.logged_in = False
#         st.session_state.pop("username", None)
#         st.rerun()

# else:
#     page = st.radio(
#         "Choose an option",
#         ["Login", "Register"],
#         horizontal=True
#     )

#     username = st.text_input("Username")
#     password = st.text_input(
#         "Password",
#         type="password"
#     )

#     if page == "Register":
#         if st.button("Create Account"):
#             success, message = register_user(
#                 username, password
#             )

#             if success:
#                 st.success(message)
#             else:
#                 st.error(message)

#     else:
#         if st.button("Login"):
#             if verify_user(username, password):
#                 st.session_state.logged_in = True
#                 st.session_state.username = username.strip()
#                 st.rerun()
#             else:
#                 st.error("Invalid username or password.")



# ******************************Generate password*************************************

# import random
# import string

# st.set_page_config(page_title="Password Generator")

# st.title("Secute Password Generator")
# st.write("Generate strong and secure password based on your preference")

# length = st.slider("Password Length",min_value=6,max_value=32,value=12)
# include_digits = st.checkbox("Include digits(0-9)",value=True)
# include_symbols = st.checkbox("Include symbols(!,@,#...)",value=True)
# include_uppercase = st.checkbox("Include Upper letters (A-Z)" ,value=True)
# include_lowercase = st.checkbox("Include Lower letters (a-z)" ,value=True)

# if st.button("Generate Password"):

#     characters = ""

#     if include_digits:
#         characters += string.digits

#     if include_symbols:
#         characters += string.punctuation

#     if include_uppercase:
#         characters += string.ascii_uppercase

#     if include_lowercase:
#         characters += string.ascii_lowercase

#     if not characters:
#         st.error("Please select at least one character type.")

#     else:
#         password = "".join(
#             random.choice(characters)
#             for _ in range(length)
#         )

#         st.success("Your password is generated!")
#         st.code(password)

#         st.download_button(
#             "Download Password",
#             data=password,
#             file_name="password.txt",
#             mime="text/plain"
#         )



# ******************************************************************

# import streamlit as st
# import requests
# import pandas as pd
# import plotly.express as px

# st.set_page_config(
#     page_title="City Temperature Dashboard",
#     page_icon="🌦️",
#     layout="wide"
# )

# st.title("🌦️ City Temperature Dashboard")
# st.write("Check current weather and temperature by city.")

# # City selection
# cities = {
#     "Mumbai": (19.0760, 72.8777),
#     "Pune": (18.5204, 73.8567),
#     "Bengaluru": (12.9716, 77.5946),
#     "Delhi": (28.6139, 77.2090),
#     "Chennai": (13.0827, 80.2707),
#     "Hyderabad": (17.3850, 78.4867),
#     "Kolkata": (22.5726, 88.3639),
#     "London": (51.5072, -0.1276),
#     "New York": (40.7128, -74.0060)
# }

# selected_city = st.sidebar.selectbox(
#     "Select City",
#     list(cities.keys())
# )

# latitude, longitude = cities[selected_city]

# # Fetch current weather
# if st.button("Get Weather"):

#     try:
#         url = "https://api.open-meteo.com/v1/forecast"

#         params = {
#             "latitude": latitude,
#             "longitude": longitude,
#             "current": (
#                 "temperature_2m,"
#                 "relative_humidity_2m,"
#                 "apparent_temperature,"
#                 "wind_speed_10m,"
#                 "weather_code"
#             ),
#             "hourly": "temperature_2m",
#             "forecast_days": 1,
#             "timezone": "auto"
#         }

#         response = requests.get(
#             url,
#             params=params,
#             timeout=15
#         )
#         response.raise_for_status()
#         data = response.json()

#         current = data["current"]

#         st.subheader(f"📍 Weather in {selected_city}")
#         st.caption(f"Local observation time: {current['time']}")

#         # Weather metrics
#         col1, col2, col3, col4 = st.columns(4)

#         col1.metric(
#             "🌡️ Temperature",
#             f"{current['temperature_2m']} °C"
#         )

#         col2.metric(
#             "🤗 Feels Like",
#             f"{current['apparent_temperature']} °C"
#         )

#         col3.metric(
#             "💧 Humidity",
#             f"{current['relative_humidity_2m']}%"
#         )

#         col4.metric(
#             "💨 Wind Speed",
#             f"{current['wind_speed_10m']} km/h"
#         )

#         # Hourly temperature chart
#         st.subheader("Hourly Temperature Forecast")

#         hourly = data["hourly"]

#         df = pd.DataFrame({
#             "Time": pd.to_datetime(hourly["time"]),
#             "Temperature (°C)": hourly["temperature_2m"]
#         })

#         fig = px.line(
#             df,
#             x="Time",
#             y="Temperature (°C)",
#             markers=True,
#             title=f"Temperature Today - {selected_city}"
#         )

#         st.plotly_chart(
#             fig,
#             use_container_width=True
#         )

#         st.subheader("Hourly Weather Data")
#         st.dataframe(df, use_container_width=True)

#     except requests.RequestException as e:
#         st.error(f"Unable to fetch weather data: {e}")

#     except (KeyError, ValueError) as e:
#         st.error(f"Unexpected weather data format: {e}")

# else:
#     st.info("Select a city and click Get Weather.")


# *******************stock price**************


# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import plotly.express as px

# st.set_page_config(
#     page_title="Stock Price Dashboard",
#     page_icon="📈",
#     layout="wide"
# )

# st.title("📈 Stock Price Dashboard")
# st.write("Explore stock prices and historical trends.")

# # Stock selection
# stock_options = {
#     "Reliance Industries": "RELIANCE.NS",
#     "TCS": "TCS.NS",
#     "Infosys": "INFY.NS",
#     "HDFC Bank": "HDFCBANK.NS",
#     "ICICI Bank": "ICICIBANK.NS",
#     "Apple": "AAPL",
#     "Microsoft": "MSFT",
#     "NVIDIA": "NVDA"
# }

# company = st.sidebar.selectbox(
#     "Select Company",
#     list(stock_options.keys())
# )

# ticker = stock_options[company]

# period = st.sidebar.selectbox(
#     "Select Period",
#     ["1mo", "3mo", "6mo", "1y", "5y"],
#     index=3
# )

# if st.button("Get Stock Data"):

#     try:
#         with st.spinner("Fetching stock data..."):
#             df = yf.Ticker(ticker).history(period=period)

#         if df.empty:
#             st.error("No stock data found. Try again later.")
#             st.stop()

#         df = df.reset_index()

#         # Latest available closing price
#         latest_price = df["Close"].iloc[-1]
#         previous_price = (
#             df["Close"].iloc[-2]
#             if len(df) > 1 else latest_price
#         )

#         change = latest_price - previous_price
#         change_percent = (
#             change / previous_price * 100
#             if previous_price else 0
#         )

#         # Dashboard metrics
#         col1, col2, col3 = st.columns(3)

#         col1.metric(
#             "Latest Closing Price",
#             f"{latest_price:,.2f}",
#             f"{change_percent:+.2f}%"
#         )

#         col2.metric(
#             "Highest Price",
#             f"{df['High'].max():,.2f}"
#         )

#         col3.metric(
#             "Lowest Price",
#             f"{df['Low'].min():,.2f}"
#         )

#         # Historical price chart
#         st.subheader(f"{company} - Price History")

#         fig = px.line(
#             df,
#             x="Date",
#             y="Close",
#             title="Closing Price Trend",
#             labels={
#                 "Date": "Date",
#                 "Close": "Closing Price"
#             }
#         )

#         st.plotly_chart(
#             fig,
#             use_container_width=True
#         )

#         # Trading volume
#         st.subheader("Trading Volume")

#         fig2 = px.bar(
#             df,
#             x="Date",
#             y="Volume",
#             title="Daily Trading Volume"
#         )

#         st.plotly_chart(
#             fig2,
#             use_container_width=True
#         )

#         # Raw data
#         st.subheader("Historical Stock Data")

#         st.dataframe(
#             df[["Date", "Open", "High", "Low",
#                 "Close", "Volume"]],
#             use_container_width=True,
#             hide_index=True
#         )

#     except Exception as e:
#         st.error(f"Unable to fetch stock data: {e}")


# ******************************Map***************************************



# import streamlit as st
# import folium
# from geopy.geocoders import Nominatim
# from streamlit_folium import st_folium

# st.title("Find Location on Map")

# # Store location between Streamlit reruns
# if "location_data" not in st.session_state:
#     st.session_state.location_data = None

# place = st.text_input(
#     "Enter city or address",
#     "Mumbai, Maharashtra, India"
# )

# if st.button("Find Location"):
#     try:
#         geolocator = Nominatim(
#             user_agent="my_streamlit_map_app"
#         )

#         location = geolocator.geocode(
#             place,
#             timeout=10
#         )

#         if location:
#             st.session_state.location_data = {
#                 "address": location.address,
#                 "latitude": location.latitude,
#                 "longitude": location.longitude
#             }
#         else:
#             st.session_state.location_data = None
#             st.warning("Location not found.")

#     except Exception as e:
#         st.error(f"Error: {e}")

# # Display map OUTSIDE the button condition
# data = st.session_state.location_data

# if data:
#     st.write("Address:", data["address"])
#     st.write("Latitude:", data["latitude"])
#     st.write("Longitude:", data["longitude"])

#     m = folium.Map(
#         location=[
#             data["latitude"],
#             data["longitude"]
#         ],
#         zoom_start=13
#     )

#     folium.Marker(
#         [data["latitude"], data["longitude"]],
#         popup=data["address"],
#         tooltip="Selected Location"
#     ).add_to(m)

#     st_folium(
#         m,
#         key="location_map",
#         width=700,
#         height=450
#     )

# ******************************Map***************************************

# import streamlit as st
# from streamlit_folium import st_folium
# from geopy.geocoders import Nominatim
# import folium

# # _________________________________________________________________________
# # st.title("Adding a Marker")

# # m = folium.Map(location=[48.8566,2.3533],zoom_start=12)

# # folium.Marker([48.8566,2.3522],
# #               popup="Hello from Paris!",
# #               tooltip="CLick me",
# #               icon=folium.Icon(color="red",icon="heart",prefix="fa")      
# #               ).add_to(m)

# # st_folium(m,width=700)
# # ______________________________________________________________________________

# st.title("Search a City and Add a Marker")

# city_name = st.text_input("Enter a city name: ",placeholder="e.g. Paris,Tokyo,London")

# location =[48.8566,2.3522]
# zoom = 4

# if city_name:
#     geolocator = Nominatim(user_agent="Streamlit_map_app")
#     location_data = geolocator.geocode(city_name)

#     if location_data:
#         location=[location_data.latitude,location_data.longitude]
#         zoom = 10
#         st.success(f"Found:{location_data.address}")
#     else:
#         st.error(f"City not Found! Showing default view (Paris)")

# m = folium.Map(location=location,zoom_start=zoom)

# folium.Marker(location,
#               popup=f"Hello from {city_name or 'Paris'}!",
#               tooltip="CLick me",
#               icon=folium.Icon(color="red",icon="heart",prefix="fa")      
#               ).add_to(m)

# st_folium(m,width=700,height=500)


# ******************************Remove background***************************************


# python -m pip install --upgrade googletrans==4.0.2



# import streamlit as st
# from deep_translator import GoogleTranslator

# st.title("🌐 Multi-Language Translation App")

# languages = {
#     "Hindi": "hi",
#     "Marathi": "mr",
#     "Kannada": "kn",
#     "Tamil": "ta",
#     "Telugu": "te",
#     "English": "en",
#     "French": "fr",
#     "German": "de",
#     "Spanish": "es"
# }

# text = st.text_area("Enter your text:")

# target_language = st.selectbox(
#     "Select the language to translate into:",
#     list(languages.keys())
# )

# if st.button("Translate"):
#     if not text.strip():
#         st.warning("Please enter some text.")
#     else:
#         try:
#             translated_text = GoogleTranslator(
#                 source="en",
#                 target=languages[target_language]
#             ).translate(text.strip())

#             st.subheader("Translated Text")
#             st.write(translated_text)

#         except Exception as e:
#             st.error(f"Translation failed: {e}")



import psutil
print("Logical Cores:",psutil.cpu_count())
print("Physical Cores:",psutil.cpu_count(logical=False))
print("CPU Usage (%):",psutil.cpu_percent(interval=1))



            