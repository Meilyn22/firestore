# Overview

This program uses firebase and streamlit to create a web applications. Streamlit reduces the html and css you would have to write when creating application for the web.

I decided to use streamlit because I realized using Django or Flask for easy apps might be doing too much.
Also, pyrebase is a firestore library, it makes your life easy when it comes to using firebase. 

I have built a website where users can login, update their profile, post a picture, and interact with others on the app. This project isn't finished at the moment because streamlit I am still trying to figure out streamlit and their session state.

To run the app you would need to install streamlit and pyrebase.

`pip install streamlit`
`pip install pyrebase`

1. Open the app.py file.
2. In the terminal do this
`streamlit run app.py`

The app will automatically open your browser and display the code.
enjoy

[Software Demo Video (play in 2X speed)](https://youtu.be/uJOlDnlWwnw)

# Cloud Database

I am using cloud firestore with pyrebase.

# Development Environment

To see the items required to run the software please check the requirements.txt file.

This program was made with Python 3.10.0

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](https://github.com/thisbejim/Pyrebase)
* [Web Site Name](https://blog.streamlit.io/streamlit-firestore/)

# Future Work

* I need to fix the profile update function.
* I need to complete the homepage.
* The work feed where users can see themselves will take a while to finsh.