# -*- coding: utf-8 -*-
"""
Created on Tue MAY 12 07:10:20 2026

@author: Sanchita Jadhav
"""

import streamlit as st

st.title("Grocery Bill Calculator")

item1 = st.number_input("Price of Item 1")
item2 = st.number_input("Price of Item 2")
item3 = st.number_input("Price of Item 3")

total = item1 + item2 + item3

if st.button("Calculate Bill"):
    st.success(f"Total Grocery Bill = ₹{total}")
