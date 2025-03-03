import pandas as pd

def update_csv(new_entry, filename="registrations.csv"):
    """ Append new registration data to CSV. """
    df = pd.DataFrame([new_entry])
    try:
        existing_data = pd.read_csv(filename)
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass  # If file doesn't exist, it will be created automatically

    df.to_csv(filename, index=False)
