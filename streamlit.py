import streamlit as st
st.title("kt")
st.success("hello")
name = st.text_input("Enter Your name")
if(st.button('Submit')):
    st.write("hello")
    st.success(name)
