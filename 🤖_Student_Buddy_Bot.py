# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:29:05 2024

@author: sarathbabu.k.lv
"""

import streamlit as st
import torch
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Student Buddy Bot",
    page_icon=":robot_face:",
)

st.title(":robot_face: Student Buddy Bot")

@st.cache_resource(show_spinner=False)
def load_model():
    # model = pipeline(model="databricks/dolly-v2-7b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
    model = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
    return model

def generate_response(prompt):
    txt = "You are called Student Buddy Bot: You help students by answering their questions and guiding them through their Academic Journey\n"
    txt+= "Adam is a student who has recentry enrolled in Data Science course. He has good knowledge in programming languages such as Python,Rust and C++.\n"
    prompt = txt+prompt
    model = load_model()
    result = model(prompt)
    result = result[0]["generated_text"]
    return result

# page_bg_img = '''
# <style>
# .stApp{
# background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)


# message = """Hello Adam!!\n\n\n
# I am student buddy bot, your personalized learning bot.\n\n\n
# I'm here to help you with your studies, answer your questions, and guide you through your academic journey. Whether you're looking for homework help, study tips, or just some motivation, I'm ready to assist!\n\n\n
# Please, click on any options on the sidebar and let's make learning easier and more fun together! 😊"""

message = """Hello Adam!!\n\n\n
I am here to help. Be it concept clarification or doubts clarification or anything general😊"""

with st.chat_message("assistant"):
    st.markdown(message)
    
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

# React to user input
if prompt := st.chat_input("Enter your query here"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    print("<<<"+prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Retrieving responses..."):
        response = generate_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    print(">>>"+response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})    