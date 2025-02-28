import csv
import os

FILEPATH = "Newcommers.csv"

def update_csv(data_dict):
    """Appends a new row to the CSV file, ensuring data is saved properly."""
    file_exists = os.path.exists(FILEPATH)

    fieldnames = ["First Name", "Middle", "Last Name", "Gender", "Marital Status",
                  "If Married, Date", "Phone Number", "Date of Birth", "Email",
                  "Date Joined", "Department(s) serving",
                  "Family Relationship", "Relation First Name", "Relation Middle Name",
                  "Relation Last Name", "Relation Telephone", "Relation Email", 
                  "Children Name", "Children Contact", "Children Date of Birth", "Address",
                  "Area Location", "Occupation", "Education Level", "Institution Attended",
                  "Certification", "From", "To"]

    with open(FILEPATH, "a", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        # Ensure data_dict only contains expected keys
        filtered_data = {key: data_dict.get(key, "") for key in fieldnames}

        writer.writerow(filtered_data)  
        file.flush()  # Force write to disk
