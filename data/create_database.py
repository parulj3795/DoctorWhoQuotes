import sqlite3
import csv

# Define the path to your CSV file
csv_file_path = 'FINAL_doctor_who_quotes.csv'

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quotes.db')
cur = conn.cursor()

# Create a table for the quotes
# Adjust column definitions based on your CSV structure
cur.execute('''CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY,
                quote TEXT NOT NULL)''')

# Open the CSV file and insert each quote into the database
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Assuming each row contains a single quote in the first column
        cur.execute('INSERT INTO quotes (quote) VALUES (?)', (row[0],))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into the database.")
