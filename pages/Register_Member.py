import streamlit as st
import pandas as pd
import datetime
from functions import update_csv

st.set_page_config(layout="wide")

logo_image = 'img/logo.jpg'
st.logo(logo_image, size='large')

df = pd.read_csv('occupations.csv')


with st.form(key="form"):
    st.subheader("PERSONAL DETAILS")
    fname = st.text_input("First Name")
    mname = st.text_input("Middle")
    lname = st.text_input("Last Name")
    gender = st.radio("Gender", ["Male", "Female"], index=None)
    marital_status = st.radio("Marital status", ["Single", "Married", "Divorced", "Separated", "Widow(er)"], index=None)
    married_date = st.date_input("If Married, Date", value=None)
    phone_number = st.text_input("Phone Number")
    dob = st.date_input("Date of Birth", value=None)
    email = st.text_input("Email")
    date_joined = st.date_input("Date joined", value=None)
    department = st.text_area("Department(s) serving")
    st.subheader("FAMILY")
    family_relationship = st.selectbox("Family Relationship", ("Spouse", "Child", "Sibling", "Parent", "Guardian", "Next of Kin"),
                                        index=None, placeholder="Choose an option")
    relation_fname = st.text_input("Relation's First name")
    relation_mname = st.text_input("Relation's Middle name")
    relation_lname = st.text_input("Relation's Last name")
    relation_tel = st.text_input("Relation's Telephone")
    relation_email = st.text_input("Relation's Email")
    children_name = st.text_area("Children Name")
    children_contact = st.text_area("Children Contact")
    children_dob = st.text_area("Children Date of Birth")
    address = st.text_area("Address")
    area_location = st.text_area("Area/Location")
    occupation = st.selectbox("Occupation", (df['Occupations']), index=None, placeholder="Choose an job type")
    education_level = st.radio("Highest educational level", (
        "Basic", "'O' Level", "'A' Level", "JHS", "SHS", "Sec./Tech./Vocational", "Post Sec.", "Diploma",
        "Bachelors", "Masters or Equivalent", "Doctoral or Equivalent"), index=None)
    institution_attended = st.text_area("Enter your school here")
    certification = st.text_area("E.g. WASSCE/ Bachelors degree", placeholder="What certification do you hold? ")
    beginning_year = st.date_input("Date joined", value=None, key='year_begin')
    ending_year = st.date_input("Date completed", value=None, key='year_end')
    submit = st.form_submit_button("Submit")

if submit:
    if fname and lname and gender and dob:  # Validate required fields
        new_entry = {
            "First Name": fname.strip(),
            "Middle": mname.strip() if mname else "",
            "Last Name": lname.strip(),
            "Gender": gender if gender else "",
            "Marital Status": marital_status if marital_status else "",
            "If Married, Date": str(married_date) if married_date else "",
            "Phone Number": phone_number.strip() if phone_number else "",
            "Date of Birth": str(dob),
            "Email": email.strip() if email else "",
            "Date Joined": str(date_joined) if date_joined else "",
            "Department(s) serving": department.strip() if department else "",
            "Family Relationship": family_relationship if family_relationship else "",
            "Relation First Name": relation_fname.strip() if relation_fname else "",
            "Relation Middle Name": relation_mname.strip() if relation_mname else "",
            "Relation Last Name": relation_lname.strip() if relation_lname else "",
            "Relation Telephone": relation_tel.strip() if relation_tel else "",
            "Relation Email": relation_email.strip() if relation_email else "",
            "Children Name": children_name.strip() if children_name else "",
            "Children Contact": children_contact.strip() if children_contact else "",
            "Children Date of Birth": str(children_dob) if children_dob else "",
            "Address" : address.strip() if address else "",
            "Area Location": area_location.strip() if area_location else "",
            "Occupation" : occupation.strip() if occupation else "",
            "Education Level" : education_level.strip() if education_level else "",
            "Institution Attended": institution_attended.strip() if institution_attended else "",
            "Certification": certification.strip() if certification else "",
            "From": str(beginning_year) if beginning_year else "",
            "To": str(ending_year) if ending_year else "" 
        }

        update_csv(new_entry)
        st.success("Record saved successfully")
    else:
        st.error("Please fill in all required fields (First Name, Last Name, Gender, Date of Birth)")
