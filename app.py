#Import necessary libraries needed for this application
import pyrebase
import streamlit as st
from datetime import datetime

firebaseConfig = {
  'apiKey': "AIzaSyCI4ktQtd__neMDF8TmTh6-6fLebaKvpGc",
  'authDomain': "connectdbtopython.firebaseapp.com",
  'projectId': "connectdbtopython",
  'storageBucket': "connectdbtopython.appspot.com",
  'messagingSenderId': "851855818440",
  'appId': "1:851855818440:web:fbcbaa9cc208bfc92e6ffd",
  'measurementId': "G-J7FFLQY5H9",
  'databaseURL': "https://connectdbtopython-default-rtdb.firebaseio.com"
}

#Initialize application

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#create database

db = firebase.database()


#create storage

storage = firebase.storage()

#Create visual sidebar with streamlit


st.sidebar.title("Community App")

#Authenticate username and password

choice = st.sidebar.selectbox("Login/signup", ["login", "sign up"])


email = st.sidebar.text_input("Please provide your email")
password = st.sidebar.text_input("Please provide your password", type="password")


#create username and password for user if they don't have one.

if choice == "sign up":
  st.sidebar.info("password should be atleast 6 characters")
  handle = st.sidebar.text_input('Please input a username', value= 'default')
  submit = st.sidebar.button("create my account")

  if submit:
    try:
      user = auth.create_user_with_email_and_password(email, password)
      st.success("Your account wass created succesfully")
      st.balloons()
      #sign the user in.
      user = auth.sign_in_with_email_and_password(email, password)
      db.child(user['localId']).child("Handle").set(handle)
      db.child(user['localId']).child("ID").set(user['localId'])
      title = st.title(f"Welcome {handle}")
      st.info('Login via login drop down selection')
    except:
      st.sidebar.error("Invalid email or password")

if choice == "login":
  login = st.sidebar.checkbox('Login')

  if login:
    bio = None
    try:
      user = auth.sign_in_with_email_and_password(email, password)
      st.write("<style>div.row-widget.stRadio > div{flex-direction:row;} </style>", unsafe_allow_html=True)
      bio = st.radio('Jump to', ['Home', 'profile', 'Workplace Feeds', 'Settings'])
    except:
      st.sidebar.error("Wrong email or password")
    else:
      if bio == "profile":
        handle = db.child(user['localId']).child("Handle").get()
        st.write(f"Username: {handle.val()}")
        st.write(f"Email: {email}")


        profile = db.child(user['localId']).child("profile_data").get().val()

        if profile is not None:
          profile = db.child(user['localId']).child("profile_data").get()
          for items in profile.each():
            f = st.write(f"First Name: {items.val()['first_name']}")
            s = st.write(f"Last Name: {items.val()['last_name']}")
            t = st.write(f"About me: {items.val()['about']}")
            
        else:
          st.info("Please enter your information to complete your profile.")
          
          with st.form(key='my_form'):
            first_name = st.text_input("First Name", key="first_name")
            last_name = st.text_input("Last Name", key="last_name")
            about = st.text_input("About me", key="about")
            save_profile = st.form_submit_button(label="Update")
            if save_profile:
              p_data = {
                  "first_name": first_name,
                  "last_name": last_name,
                  "about": about
                }
              result = db.child(user['localId']).child("profile_data").push(p_data)
              st.success("Uploaded")

      if  bio == "Settings":
       
          # CHECK FOR IMAGE
          nImage = db.child(user['localId']).child("Image").get().val()    
          # IMAGE FOUND     
          if nImage is not None:
              # We plan to store all our image under the child image
              Image = db.child(user['localId']).child("Image").get()
              for img in Image.each():
                  img_choice = img.val()
                  #st.write(img_choice)
              st.image(img_choice)
              exp = st.beta_expander('Change Bio and Image')  
              # User plan to change profile picture  
              with exp:
                  newImgPath = st.text_input('Enter full path of your profile imgae')
                  upload_new = st.button('Upload')
                  if upload_new:
                      uid = user['localId']
                      fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                      a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                      db.child(user['localId']).child("Image").push(a_imgdata_url)
                      st.success('Success!')           
          # IF THERE IS NO IMAGE
          else:    
              st.info("No profile picture yet")
              newImgPath = st.text_input('Enter full path of your profile image')
              upload_new = st.button('Upload')
              if upload_new:
                  uid = user['localId']
                  # Stored Initated Bucket in Firebase
                  fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                  # Get the url for easy access
                  a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                  # Put it in our real time database
                  db.child(user['localId']).child("Image").push(a_imgdata_url)
      
    
      