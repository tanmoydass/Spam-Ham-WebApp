import streamlit as st
import joblib
 
st.header("Hey, Welcome to Spam Detector")
st.subheader("Tanmoy Das")
st.title('SPAM-HAM CLASSIFIER')#creates a title in web app
ip = st.text_input('Enter the message') #creates a text box in web app
op = model_nb.predict([ip])
if st.button('Predict'): # st.button will create a button with name Predict
  st.title(op[0]) # the output will be displayed as a title
  st.balloons()  
