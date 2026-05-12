# -*- coding: utf-8 -*-
"""
Created on Tue MAY 12 07:10:20 2026

@author: Sanchita Jadhav
"""
import streamlit as st

st.title("BMI Health Checker")

weight = st.number_input("Enter your weight (kg)")
height = st.number_input("Enter your height (meters)")

if st.button("Check BMI"):

    bmi = weight / (height ** 2)

    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.warning("Underweight")

    elif bmi < 25:
        st.success("Normal Weight")

    elif bmi < 30:
        st.warning("Overweight")

    else:
        st.error("Obese")
