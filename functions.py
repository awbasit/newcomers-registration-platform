import csv
import os

FILEPATH = "Newcommers.csv"

def get_csv():
    """Reads CSV file and returns data as a list of dictionaries."""
    if not os.path.exists(FILEPATH):  # Check if the file exists
        return []

    with open(FILEPATH, "r", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def update_csv(data):
    """Appends a new row to the CSV file, creating it if necessary."""
    file_exists = os.path.exists(FILEPATH)  # Check if the file exists before writing

    with open(FILEPATH, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # If file doesn't exist, write the header first
        if not file_exists:
            writer.writerow(["Name", "Address", "Contact", "Email", 
                             "Are you a born again Christian?", "Do you want to Church?", 
                             "How did you hear about us?"])
        
        writer.writerow(data)  # Append new entry

if __name__ == "__main__":
    print("Hello")
