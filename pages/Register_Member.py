import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from functions import update_csv
import json

st.set_page_config(layout="wide")

# Load Google Sheets API credentials
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
# Load credentials from Streamlit Secrets
creds_dict = st.secrets["google_credentials"]

#streamlit secrets return dictionary so no need to use json.load()
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

# Authorize Google Sheets API
client = gspread.authorize(creds)

# Open Google Sheet (Replace with your actual Google Sheet ID)
SHEET_ID = st.secrets["google_credentials"]["SHEET_ID"]
sheet = client.open_by_key(SHEET_ID).worksheet("Sheet1")

# Load occupations from CSV
df = pd.read_csv('occupations.csv')

# Streamlit UI
logo_image = 'img/logo.jpg'
st.image(logo_image, width=200)

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

    # Ensure Occupation dropdown loads correctly
    occupation_list = df['Occupations'].tolist()
    occupation = st.selectbox("Occupation", occupation_list, index=None, placeholder="Choose a job type")

    education_level = st.radio("Highest educational level", (
        "Basic", "'O' Level", "'A' Level", "JHS", "SHS", "Sec./Tech./Vocational", "Post Sec.", "Diploma",
        "Bachelors", "Masters or Equivalent", "Doctoral or Equivalent"), index=None)
    institution_attended = st.text_area("Enter your school here")
    certification = st.text_area("E.g. WASSCE/ Bachelors degree", placeholder="What certification do you hold?")
    beginning_year = st.date_input("Date joined", value=None, key='year_begin')
    ending_year = st.date_input("Date completed", value=None, key='year_end')
    submit = st.form_submit_button("Submit")

if submit:
    if fname and lname and gender and dob:  # Validate required fields
        # Define column names for Google Sheets
        column_headers = [
            "First Name", "Middle Name", "Last Name", "Gender", "Marital Status",
            "If Married, Date", "Phone Number", "Date of Birth", "Email", "Date Joined",
            "Department(s) Serving", "Family Relationship", "Relation First Name", 
            "Relation Middle Name", "Relation Last Name", "Relation Telephone", "Relation Email",
            "Children's Names", "Children's Contact", "Children's Date of Birth",
            "Address", "Area Location", "Occupation", "Education Level", 
            "Institution Attended", "Certification", "Start Year", "Completion Year"
        ]
        # Prepare data in the correct order
        new_entry = [
            fname.strip(),
            mname.strip() if mname else "",
            lname.strip(),
            gender if gender else "",
            marital_status if marital_status else "",
            str(married_date) if married_date else "",
            phone_number.strip() if phone_number else "",
            str(dob),
            email.strip() if email else "",
            str(date_joined) if date_joined else "",
            department.strip() if department else "",
            family_relationship if family_relationship else "",
            relation_fname.strip() if relation_fname else "",
            relation_mname.strip() if relation_mname else "",
            relation_lname.strip() if relation_lname else "",
            relation_tel.strip() if relation_tel else "",
            relation_email.strip() if relation_email else "",
            children_name.strip() if children_name else "",
            children_contact.strip() if children_contact else "",
            children_dob.strip() if children_dob else "",
            address.strip() if address else "",
            area_location.strip() if area_location else "",
            occupation.strip() if occupation else "",
            education_level.strip() if education_level else "",
            institution_attended.strip() if institution_attended else "",
            certification.strip() if certification else "",
            str(beginning_year) if beginning_year else "",
            str(ending_year) if ending_year else ""
        ]

        # Check if headers exist in Google Sheets; if not, add them
        existing_headers = sheet.row_values(1)
        if not existing_headers:
            sheet.append_row(column_headers)
        # Append data to Google Sheet
        sheet.append_row(new_entry)
        st.success("Registration successful! ✅")

    else:
        st.error("Please fill in all required fields (First Name, Last Name, Gender, Date of Birth)")

    update_csv(dict(zip(column_headers, new_entry)))
# df.to_csv("members.csv", index=False)
