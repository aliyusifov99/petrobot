import streamlit as st
import ast
import pandas as pd
from open_ai_inquirer import OpenAIInquirer

embeddings_path = 'https://raw.githubusercontent.com/aliyusifov99/petrobot/main/petrel_manual.csv'
df = pd.read_csv(embeddings_path)
df['embedding'] = df['embedding'].apply(ast.literal_eval)

    
st.markdown("<h1 style='text-align: center;'>PetroBot🛢️</h1>", unsafe_allow_html=True)
st.write("Don't spend hours on software manuals. New AI based chatbot 'PetroBot' will do it for you!")
st.header("",divider='rainbow')
text = st.text_area(placeholder = 'Send a message', label = '')




def show_message(txt:str):
    if len(txt)==0:
        print('')    
    else:
        inquirer = OpenAIInquirer(text=txt, df=df, api_key=st.secrets['auth_key'])
        response = inquirer.inquire()
        st.write(response)
    
    

button = st.button('Send',on_click=show_message(text))