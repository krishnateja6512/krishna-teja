import streamlit as st
st.title("kt")
st.header("This is a header")
st.subheader("This is a subheader")
st.success("hello")
name = st.text_input("Enter Your name")
if(st.button('Submit')):
    result = name.title()
    st.success(result)