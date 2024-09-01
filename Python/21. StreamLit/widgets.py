import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

age = st.slider('Select your age: ', 0, 100, 25)
st.write(f'Your age is: {age}')
name = st.text_input("Enter your name: ")
if name:
    st.write(f'Hello, {name}')
    
    
options = ['Python', 'JavScript', 'Java', 'C', 'C++']
choice = st.selectbox("Choose your favorite language: ", options)
st.write(f'You Selected: {choice}')

df = pd.DataFrame({
    '1st column': [1, 2, 3, 4],
    '2nd column': [5, 6, 7, 8]
})

df = pd.DataFrame(df)
df.to_csv('sample_data.csv')
st.write(df)

uploaded_file = st.file_uploader('Chose a csv file', type = 'csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)