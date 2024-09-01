import streamlit as st
import pandas as pd 
import numpy as np

# Title of application
st.title('Hello Streamlit')

# Display Simple Text
st.write('This is a Simple text')

# Creating a dF
df = pd.DataFrame({
    '1st column': [1, 2, 3, 4],
    '2nd column': [5, 6, 7, 8]
})

# Display the dataFrame
st.write("Here is the DataFrame:")
st.write(df)

# creating a linechart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), 
    columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)