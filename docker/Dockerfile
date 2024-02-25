FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /main

# Copy the requirements file into the container to install Python dependencies
COPY ../requirements.txt /main/
RUN pip install --no-cache-dir -r /main/requirements.txt

# Copy project
COPY . /main/

# Command to run the application
CMD ["uvicorn", "dwquotes_api:app", "--host", "0.0.0.0", "--port", "80"]
