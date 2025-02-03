import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide")
st.title("Newcomers Page")

col1, col2 = st.columns(2)

with col1:
    st.image("img/photo.jpg")

with col2:
    comment="""
You are welcome to the family, Grace Impact Ministries. This is the official dwelling of God.
I am the founder and overseer. We are delighted to have your details so that we can communicate
further.
Grace unto you.
"""
    st.info(comment)

st.header("New Members")

df = pd.read_csv("Newcommers.csv")

# Drop empty columns
df = df.dropna(how="all")

# Split DataFrame into two approximately equal parts
half = len(df) // 2  # Find the middle index

df_col3, df_col4 = np.array_split(df, [half])  # Splitting dynamically

# Create two columns
col3, col4 = st.columns(2)

# Function to display records
def display_records(column, data):
    with column:
        for _, row in data.iterrows():
            st.subheader(row["Name"].title())
            st.write(row["Address"])
            st.write(row["Contact"])
            st.write(row["Email"])
            st.write(row["Are you a born again Christian?"].title())
            st.write(row["How did you hear about us?"])
            st.markdown("---")  # Adds a line separator for better readability

# Display records evenly
display_records(col3, df_col3)
display_records(col4, df_col4)