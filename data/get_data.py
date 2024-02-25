# Import the necessary libraries for making HTTP requests, parsing HTML content, and working with CSV files
import requests
from bs4 import BeautifulSoup
import csv
import re

# The URL of the Wikiquote page for "The Doctor", from which quotes will be scraped
url = "https://en.wikiquote.org/wiki/The_Doctor"

def clean_quote(quote):
    # Pattern to identify reference info patterns like " - The Big Bang 5.13 (26 June 2010)"
    # Adjust the pattern as needed to match the specifics of your data
    pattern = r"\s+-\s+[^-]+(\d+\.\d+)\s+\(\d+\s+\w+\s+\d{4}\)"
    cleaned_quote = re.sub(pattern, "", quote)
    return cleaned_quote

def clean_text(text):
    # Fix spaces before punctuation
    text = re.sub(r'\s+([,.!?])', r'\1', text)
    # Ensure space after punctuation if not followed by a space or end of string
    text = re.sub(r'([,.!?])(\w)', r'\1 \2', text)
    return text

# Define a function to scrape the quotes that are specifically in the first <li> in the first <ul> for all <ul> tags
def scrape_and_get_quotes(url):
    # Make an HTTP GET request to the provided URL and store the response
    response = requests.get(url)
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize an empty list to store the quotes extracted from the page
    quotes = []
    
    # Iterate through each 'ul' element found in the document
    for ul in soup.find_all('ul'):
        first_li = ul.find('li')  # Find the first 'li' element within the current 'ul'
        if first_li:
            # Remove any nested 'ul' elements to exclude them from the output
            for nested_ul in first_li.find_all('ul'):
                nested_ul.decompose()

            quote_text = first_li.get_text(separator=" ", strip=True)
            # Clean up the collected quote text and add it to the list if it's not empty
            cleaned_quote = clean_quote(quote_text)  # Clean the quote to remove reference info
            cleaned_quote = clean_text(' '.join(cleaned_quote.split()).strip())
            if cleaned_quote:
                quotes.append(cleaned_quote)

    return quotes

# Call the function to scrape bold quotes from the specified URL and store the result in a variable
quotes = scrape_and_get_quotes(url)

# Open (or create) a CSV file named 'doctor_who_quotes.csv' for writing
with open('doctor_who_quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Initialize a CSV writer object to write data into the CSV file
    writer = csv.writer(csvfile)
    # Iterate over each quote in the list of extracted quotes
    for quote in quotes:
        writer.writerow([quote])  # Write each quote as a new row in the CSV file

# Print the number of bold quotes collected and saved to the CSV file
print(f"Collected {len(quotes)} quotes. Now clean manually.")
