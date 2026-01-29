import streamlit as st
st.title("Streamlit Application")
st.header("Streamlit Applicatio")
st.subheader("Streamlit Applicati")
st.text("Streamlit Applicat")
st.write("Streamlit Applica")
st.markdown("Streamlit Applic")
st.caption("Streamlit Appli")

name = st.text_input("enter your name")
st.write("your name is ",name)

age = st.number_input("Enter age",18,65,29)

gender = st.radio("Gender",["Male","Female","Other"])
dob = st.date_input("Select DOB")
hobby = st.multiselect("Hobbies",["Reading","Sports","Music"])
Submit = st.button("Submit")

values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

import pandas as pd
df = pd.DataFrame({
        "Name" : ["A","B","C"],
        "Age" : [20,28,29]
})
st.dataframe(df)

st.bar_chart(df)
st.bar_chart(df,x="Name",y="Age")

line_chart_data = pd.DataFrame ({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 120, 200, 180, 220],
    "Expenses": [80, 90, 100, 110, 120, 130]
})
st.line_chart(line_chart_data, x="Month", y=["Sales", "Expenses"])