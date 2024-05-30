import streamlit as st

 # Title of the app
st.title("Student Information ")
name = st.text_input("Enter the student's name")
age = st.slider("Select the student's age",min_value=1,max_value=100)
#st.button("Display information",on_click= name)
#st.text("Student's name:", name)
if st.button("Display information"):
    st.write("Student's name: ", name)
    st.write("Student's age: ", age)