import streamlit as st
import pandas as pd
st.title("Веб-приложение на питоне")
name = st.text_input("Введите имя", "")
st.write(f"Привет, {name}!")
x = st.slider("Выберите x", 0, 10, 1)
y = st.slider("Выберите y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["1"])
st.write(df)
