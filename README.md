# Doctor Who Quotes API

This repository contains the Doctor Who Quotes API, a FastAPI application designed to serve memorable quotes from the iconic Doctor Who series. 
It represents my first venture into API development and web scraping, combining my interest in software development with my love for Doctor Who.

## Project Overview

The Doctor Who Quotes API provides endpoints to retrieve random quotes or specific quotes by ID. It's built using FastAPI and SQLite, with quotes 
collected through web scraping techniques. This project serves as a practical example of how to design and deploy a RESTful API from scratch.

## Features

- **Random Quote**: Fetch a random Doctor Who quote.
- **Quote by ID**: Retrieve a specific quote using its unique identifier.

## Technologies

- FastAPI for the web framework.
- SQLite for the lightweight database solution.
- Docker for containerization and easy deployment.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or later
- Docker (for containerization, coming soon)

### Installation

1. Clone the repository:
2. Navigate to the project directory:
    ```sh
    cd doctor-who-quotes-api
3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
4. Run the FastAPI application using Uvicorn:
   ```sh
   uvicorn main:app --reload
   
Access the API at: http://localhost:8000

### Dockerization (Coming Soon)

Docker support will be added soon, allowing for easy deployment and scaling of the application.

## Usage

The API provides the following endpoints:
- /: The root endpoint, displaying a welcome message and guidance on using the API.
- /quotes/random: Returns a random Doctor Who quote.
- /quotes/{quote_id}: Retrieves a specific quote by its ID.

## License

Distributed under the MIT License. See LICENSE for more information.

## Acknowledgements

Thanks to the FastAPI team for creating such a fantastic framework.
A nod to the creators and writers of Doctor Who for providing endless inspiration.
