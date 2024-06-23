import streamlit as st
import requests

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)


data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()

st.write(data)
