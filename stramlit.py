import streamlit as st
import pandas as pd
st.title('My First app')
st.header('lol')
st.write(""" Bienvenidos a mi pagina""")

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)
st.title('Read.csv')

st.dataframe(names_data)