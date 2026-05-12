# -*- coding: utf-8 -*-
"""
Created on Tue MAY 12 07:10:20 2026

@author: Sanchita Jadhav
"""
import streamlit as st

st.title("Student Result Calculator")

sub1 = st.number_input("Enter marks for Subject 1", 0, 100)
sub2 = st.number_input("Enter marks for Subject 2", 0, 100)
sub3 = st.number_input("Enter marks for Subject 3", 0, 100)

total = sub1 + sub2 + sub3
percentage = total / 3

if st.button("Calculate Result"):

    st.write("Total Marks:", total)
    st.write("Percentage:", percentage)

    if percentage >= 40:
        st.success("Result: Pass")

    else:
        st.error("Result: Fail")
