import os 
from apikey import apikey 

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🦜🔗 Connor\'s AI')
prompt = st.text_input('Enter prompt here')

# Promte templates
title_template = PromptTemplate(
    input_variable = ['topic'],
    template = 'write me a youtube video title about {topic}'
)

# Script templates
script_template = PromptTemplate(
    input_variable = ['title'],
    template = 'write me a youtube video script based on this title TITLE: {title}'
)

# LLMs
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose = True, output_key = 'title')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose = True, output_key='script')
sequential_chain = SequentialChain(chains=[title_chain, script_chain], input_variables=['topic'], output_variables=['title', 'script'], verbose = True)

# Show stuff to the screen if there's a prompt
if prompt:
    response = sequential_chain({'topic':prompt})
    st.write(response['title'])
    st.write(response['script'])

#test commit 