import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0, format="%f")
num2 = st.number_input("Enter the second number", value=0.0, format="%f")

# Operation selection
operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform calculation based on the selected operation
result = None
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero")

# Display the result
if result is not None:
    st.write(f"The result of {operation} is: {result}")

# Additional reset functionality
if st.button("Reset"):
    st.experimental_rerun()
