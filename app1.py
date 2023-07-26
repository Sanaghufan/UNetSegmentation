# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:41:42 2023

@author: sana
"""

# pip install streamlit --user

import streamlit as st
import test_model
from PIL import Image

st.set_page_config(layout="wide")
st.title("Nuclie Segementation App")

img = st.sidebar.selectbox(
    "Select Image", ("Dataset/img1.png",
                     "Dataset/img2.png",
                     "Dataset/img3.png",
                    )
)

input_image =  img

image = Image.open(input_image)
st.image(image, width=400)

detect_mask = st.button("Detect Mask")

if detect_mask:
    mask = test_model.do_pred(input_image)
    st.write("Predicted Mask")
    st.image(mask, width=500)
