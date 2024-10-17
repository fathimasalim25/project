import streamlit as st
st.title("prediction")
import numpy as np 
import pandas as pd
import streamlit as st

import streamlit as st

# Create input fields for two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Sum the two numbers
result = num1 + num2

# Display the result
st.write(f"The sum of {num1} and {num2} is: {result}")

