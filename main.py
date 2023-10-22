import streamlit as st
import ast
import pandas as pd
from open_ai_inquirer import OpenAIInquirer

embeddings_path = 'https://raw.githubusercontent.com/aliyusifov99/petrobot/main/petrel_manual.csv'
df = pd.read_csv(embeddings_path)
df['embedding'] = df['embedding'].apply(ast.literal_eval)

# Title and introduction
st.markdown("<h1 style='text-align: center;'>PetroBot🛢️</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center;">
        Empower your workflow with PetroBot, the AI assistant that revolutionizes 
        the way you interact with software manuals. Save time and boost efficiency 
        by getting answers instantly, right when you need them.
    </div>
    """, 
    unsafe_allow_html=True
)

# Highlighting the support for Petrel software
st.markdown(
    """
    <div style="text-align: center; margin: 20px 0;">
        <h6 style="color: #555;"><strong>Currently Supporting:</strong></h6>
        <img src="https://seeklogo.com/images/S/schlumberger-petrel-software-simulation-logo-5F80386A5D-seeklogo.com.png" alt="Petrel logo" style="width:30px;">
    </div>
    """, 
    unsafe_allow_html=True
)


text = st.text_area(placeholder = 'Send a message', label = '')




def show_message(txt:str):
    if len(txt)==0:
        print('')    
    else:
        inquirer = OpenAIInquirer(text=txt, df=df, api_key=st.secrets['auth_key'])
        response = inquirer.inquire()
        st.write(response)
    
    

button = st.button('Send',on_click=show_message(text))

footer = """
<!-- Include FontAwesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<div style="position: fixed; bottom: 10px; left: 10px; width: 100%; padding: 10px; text-align: center;"> <!-- You can change the background-color -->
    <h5 style="color: #000000; margin-bottom: 5px;">Connect with me</h5> <!-- Header text -->
    <a href="https://github.com/aliyusifov99" target="_blank" style="text-decoration: none;">
        <i class="fa fa-github" style="font-size: 20px; color: black; margin: 0 10px;"></i> <!-- Larger icon size and spacing -->
    </a>
    <a href="https://www.linkedin.com/in/ali-yusifov/" target="_blank" style="text-decoration: none;">
        <i class="fa fa-linkedin" style="font-size: 20px; color: #0077b5; margin: 0 10px;"></i> <!-- Larger icon size and spacing -->
    </a>
    <a href="https://twitter.com/aliyusifovpy" target="_blank" style="text-decoration: none;">
        <i class="fa fa-twitter" style="font-size: 20px; color: #1DA1F2; margin: 0 10px;"></i> <!-- Larger icon size and spacing -->
    </a>
    <a href="https://www.datascienceportfol.io/aliyusifov" target="_blank" style="text-decoration: none;">
        <i class="fa fa-globe" style="font-size: 20px; color: green; margin: 0 10px;"></i> <!-- Larger icon size and spacing -->
    </a>
</div>
"""

# Render the HTML
st.markdown(footer, unsafe_allow_html=True)
