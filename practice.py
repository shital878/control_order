
import streamlit as st
import os
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

