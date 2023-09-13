import os 
from apikey import apikey 

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🦜🔗 Connors ai')
prompt = st.text_input('Enter prompt here')
