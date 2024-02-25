import csv

# Path to your CSV file
csv_file_path = 'FINAL_doctor_who_quotes.csv'

# Initialize an empty list to store the quotes
quotes = []

# Open the CSV file for reading
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Assuming each row contains a single quote
        if row:  # Check if the row is not empty
            quotes.append(row[0])  # Add the quote to the list

print(quotes[247])