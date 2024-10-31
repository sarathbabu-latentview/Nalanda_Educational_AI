# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:29:05 2024

@author: sarathbabu.k.lv
"""

import streamlit as st
import re
import torch
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')



st.set_page_config(
    page_title="PathWise",
    page_icon=":compass:",
)


st.title(":compass: PathWise")

@st.cache_resource(show_spinner=False)
def load_model():
    # model = pipeline(model="databricks/dolly-v2-7b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
    model = pipeline(model="databricks/dolly-v2-3b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto")
    return model

def generate_response(prompt):
    model = load_model()
    result = model(prompt)
    result = result[0]["generated_text"]
    return result


tab1, tab2, tab3 = st.tabs(["Machine Learning", "Deep Learning", "Artificial Intelligence"])

with tab1:
    tab11,tab12 = st.tabs(['Basics of Machine Learning','Gentle intro to Machine Learning'])
    # col1,col2 = st.columns(2)
    
    with tab11:
        with open('Introduction_to_machine_learning.txt', 'r') as file:
            data = file.read()
            context = re.sub("[^a-zA-Z]","\n",data)
            context = context.split("\n")
            context = list(filter(None,context))
            context = " ".join(context)
            context = context[:3000]
            
        col11,col12 = st.columns(2)
        col11.video(data="https://www.youtube.com/watch?v=ukzFI9rgwfU")

        
        with col12:
            with st.popover("Video transcription"):
                with open('Introduction_to_machine_learning.txt', 'r') as file:
                    data = file.read()
                    transcript = data.replace("#","").replace("\n","\n\n")
                    st.markdown(transcript)
    
    with tab12:
        # with open('Gentle_intro_to_machine_learning.txt', 'r') as file:
        #     data = file.read()
        #     context = re.sub("[^a-zA-Z]","\n",data)
        #     context = context.split("\n")
        #     context = list(filter(None,context))
        #     context = " ".join(context)
        #     context = context[:2000]
            
        col21,col22 = st.columns(2)
        col21.video(data="https://www.youtube.com/watch?v=Gv9_4yMHFhI")
        
            
        with col22:
            with st.popover("Video transcription"):
                with open('Gentle_intro_to_machine_learning.txt', 'r') as file:
                    data = file.read()
                    transcript = data.replace("#","").replace("\n","\n\n")
                    st.markdown(transcript)


message = "Adam, You can ask queries about the video to understand better."

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
    print(f"<<<context:{context}\n\nquestion:{prompt}")
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Retrieving responses..."):
        prompt = f""""context:{context}\n\nquestion:{prompt}"""
        response = generate_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    print(">>>"+response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})    
