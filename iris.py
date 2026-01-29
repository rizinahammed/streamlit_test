import streamlit as st
import numpy as np
import pickle


with open("model.pickle", "rb") as f:
    model = pickle.load(f)

st.title("Iris species prediction app")


sepal_length = st.number_input("Sepal Length", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
sepal_width  = st.number_input("Sepal Width",  min_value=0.0, max_value=10.0, value=0.0, step=0.1)
petal_length = st.number_input("Petal Length", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
petal_width  = st.number_input("Petal Width",  min_value=0.0, max_value=10.0, value=0.0, step=0.1)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)

    st.success(f"Predicted species is: {prediction[0]}")
