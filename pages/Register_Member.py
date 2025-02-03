import streamlit as st
from functions import update_csv

st.set_page_config(layout="wide")


with st.form(key="form"):
    name = st.text_input("Name")
    address = st.text_input("Address")
    email = st.text_input("Email")
    born_again = st.selectbox("Are you a born again Christian?", ("Yes", "No"), index=None, placeholder="Select one")
    join_church = st.selectbox("Do you want to join the church?", ("Yes", "No"), index=None, placeholder="Select one")
    heard_about = st.selectbox("How did you hear about us?", ("Advert", "Posters", "Billboard", "A friend", "Social Media", "Radio", "TV"), index=None, placeholder="Select one")
    submit = st.form_submit_button("Submit")

if submit:
    if name and address:  # Validate required fields
        new_entry = [name, address, "N/A", email, born_again, join_church, heard_about]  
        update_csv(new_entry)
        st.success("Record saved successfully")
    else:
        st.error("Please fill in all required fields (Name, Address)")