
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

#30)------------------Multiple pages----------------------------------------------------------------
