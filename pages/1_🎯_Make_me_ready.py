# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:29:05 2024

@author: sarathbabu.k.lv
"""

import streamlit as st
import os
import shutil

st.set_page_config(
    page_title="Make me ready",
    page_icon=":dart:",
)


st.title(":dart: Make me ready")


clicked = st.button("Fundamentals of Machine Learning")

if clicked:
    st.markdown("button has been clicked")
    src = os.getcwd()+"\\4_Learning_Path_Courses.py"
    dst = os.getcwd()+"\\pages\\4_Learning_Path_Courses.py"
    shutil.move(src, dst)
    st.switch_page("pages/4_Learning_Path_Courses.py")
    
    
    

