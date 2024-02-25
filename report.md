# Project Report: Doctor Who Quotes API

## Overview
The Doctor Who Quotes API is a web-based application designed to serve memorable quotes from the iconic British TV series, Doctor Who. This project combines the power of FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.10+ based on standard Python type hints, with the simplicity and efficiency of SQLite, a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. The application is containerised using Docker, ensuring consistency across different development and production environments.

## Objective
The primary objective of this project was to develop my first API and web scraping application, leveraging my passion for Doctor Who. The goal was to create an accessible, easy-to-use API that allows fans and developers alike to retrieve quotes from the series, either randomly or by specific IDs, thereby promoting the series' rich dialogue history in applications, websites, and fan projects.

## Technologies Used
- **FastAPI**: Selected for its high performance and ease of use for creating RESTful APIs. FastAPI's automatic interactive API documentation, data validation, and serialisation capabilities significantly streamlined the development process.
- **SQLite**: Chosen for its simplicity, portability, and suitability for small to medium-sized projects. SQLite stores the entire database (definitions, tables, indexes, and the data itself) as a single cross-platform file, making it perfect for our use case.
- **Docker**: Used for containerising the application, Docker encapsulates the application and its environment, making deployment straightforward and eliminating the "it works on my machine" problem.
- **GitHub**: Hosts the source code and facilitates version control. It also serves as the platform for continuous integration and deployment workflows.

## Application Design
The application's architecture is straightforward, designed to be scalable and easy to maintain. It consists of the following components:

1. API Endpoints:

    - A root endpoint (/) that provides basic information and guidance on how to use the API.
    - A random quote endpoint (/quotes/random) that returns a random Doctor Who quote.
    - A specific quote endpoint (/quotes/{quote_id}) that retrieves a quote based on its unique identifier.

2. Database Management:

    - Quotes are stored in an SQLite database, which the application queries to retrieve data. The simplicity of SQLite is ideal for this project's scale, providing sufficient functionality without the overhead of more complex database systems.

3. Containerisation:

    - The application is dockerised, which simplifies deployment and ensures that it runs consistently across different environments. The Docker setup includes a Dockerfile that specifies the environment, dependencies, and commands needed to run the application.

## Development Process
The development process involved several stages, from initial planning and design to development, testing, and deployment. Key development activities included:

- **Web Scraping**: Initially, quotes were collected through web scraping techniques. This process involved writing scripts to extract quotes from various online sources, then curating and formatting the data for insertion into the SQLite database. Lastly, the data was manually checked and corrected wherever needed.
- **API Development**: Leveraging FastAPI, the RESTful API endpoints were developed and tested locally. FastAPI's interactive documentation was invaluable for testing the API's functionality in real-time.
- **Database Integration**: SQLite was integrated to store and manage the quotes data. The choice of SQLite facilitated a lightweight, file-based approach to data storage, simplifying development and deployment.
- **Containerisation and Deployment Prep**: The application was containerised using Docker, and configuration files for Docker were created and tested.

## Challenges and Solutions

- **Web Scraping Complexity**: Extracting quotes from diverse sources presented challenges in handling different HTML structures and ensuring data quality. 
    - *Solution*: Customised scraping scripts were developed for each source, and data was manually reviewed for accuracy and consistency.

- **Learning Curve**: Being my first project with FastAPI and Docker, there was a learning curve. 
    - *Solution*: Extensive documentation, internet and community resources for both technologies were leveraged to accelerate the learning process.

## Conclusion and Future Directions
The Doctor Who Quotes API project successfully demonstrates the development and containerisation of a RESTful API using FastAPI and Docker. It serves as a practical example of integrating web scraping, database management, and modern API development practices.

## Future enhancements could include:

- **Expanded Database**: Incorporating more quotes and additional metadata (e.g., episode titles, air dates, characters).
- **User Contributions**: Allowing users to contribute quotes through a submission endpoint.
- **Advanced Search Capabilities**: Implementing search functionality to query quotes by character, episode, or keywords.

This project not only fulfilled its objective of creating a functional API for Doctor Who quotes but also provided valuable experience in API development, database integration, and application containerisation.




