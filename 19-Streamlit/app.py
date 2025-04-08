import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Streamlit")

st.write("This is a simple text")

## Creating a data frame

df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [6,7,8,9,0],
})

st.write("Here is the data frame")
st.write(df)

## Creating a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)
st.line_chart(chart_data)
