# Import necessary libraries and modules
from fastapi import FastAPI, HTTPException  # FastAPI for building your API, HTTPException for error handling
from typing import Optional  # Optional for optional fields in Pydantic models
from pydantic import BaseModel  # BaseModel from Pydantic for data validation and settings management
import sqlite3  # sqlite3 module for interacting with SQLite databases

# Initialize a FastAPI instance
app = FastAPI()

# Define a Pydantic model for quotes
# This model specifies the structure of a quote object, including its data types
class Quote(BaseModel):
    id: Optional[int] = None  # Quote ID (integer) is optional (might not be present for all quotes)
    quote: str  # Quote text (string) is required

# Function to establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('../data/quotes.db')  # Connect to the SQLite database named 'quotes.db'
    conn.row_factory = sqlite3.Row  # Configure the connection to return rows as dictionaries
    return conn  # Return the connection object

# Define a route for the root URL "/"
# This function returns a welcome message and instructions on how to use the API

# NOTE: 'async' - asynchronous programming paradigm which allows Python to handle asynchronous 
# operations. It's a way to write concurrent code that looks sequential. 

@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the Doctor Who Quotes API. Use /quotes/random to get a random quote or /quotes/{quote_id} to get a specific quote by its ID."
    }

# Define a route for getting a random quote
# This endpoint responds to GET requests to "/quotes/random"

# NOTE: A cursor in database terms is a database object used to perform operations 
# on the data in a database. It acts as a handle to the set of rows returned by a 
# SQL query and allows you to manage and process individual rows returned by database queries. 

@app.get("/quotes/random", response_model=Quote)
async def read_random_quote():
    conn = get_db_connection()  # Establish a database connection
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries
    # Execute an SQL query to select a random quote from the database
    cursor.execute("SELECT * FROM quotes ORDER BY RANDOM() LIMIT 1")
    quote = cursor.fetchone()  # Fetch the first (and only) row of the query result
    conn.close()  # Close the database connection
    if quote is None:  # If no quote was found (unlikely unless the database is empty)
        raise HTTPException(status_code=404, detail="No quotes found")  # Raise a 404 error
    # Convert the SQLite row to a dictionary and return it, matching the Quote model
    return {"id": quote["id"], "quote": quote["quote"]}
