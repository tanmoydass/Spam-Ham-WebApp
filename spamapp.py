import streamlit as st
import joblib
model_nb = joblib.load('spam-ham')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2015/11/08/17/10/banner-1033936_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
 
st.header("Hey, Welcome to Spam Detector")
st.subheader("Tanmoy Das")
st.title('SPAM-HAM CLASSIFIER')#creates a title in web app
ip = st.text_input('Enter the message') #creates a text box in web app
op = model_nb.predict([ip])
if st.button('Predict'): # st.button will create a button with name Predict
  st.title(op[0]) # the output will be displayed as a title
  st.balloons()  
