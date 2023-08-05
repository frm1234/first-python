import pandas as pd
import streamlit as st

weather = pd.read_csv('目前天氣.csv')
st.write('目前台灣天氣')
st.write(weather)
