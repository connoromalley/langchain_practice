import os 
from apikey import apikey 

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🦜🔗 Connor\'s AI')
prompt = st.text_input('Enter prompt here')

# LLMs
llm = OpenAI(temperature=0.9)

# Show stuff to the screen if there's a prompt
if prompt:
    response = llm(prompt)
    st.write(response)

#test commit 