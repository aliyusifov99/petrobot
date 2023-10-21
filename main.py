import streamlit as st
import openai
import os
from keys import API_KEY
from open_ai import OpenAI

    
st.markdown("<h1 style='text-align: center;'>PetroBot🛢️</h1>", unsafe_allow_html=True)
st.header("",divider='rainbow')
text = st.text_area(placeholder = 'Send a message', label = '')




def show_message(txt:str):
    if len(txt)==0:
        print('')    
    else:
        openai = OpenAI(txt)
        response = openai.generate_response()
        st.write(response)
    
    

button = st.button('Send',on_click=show_message(text))