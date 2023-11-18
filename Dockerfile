# Use an official Python runtime as a parent image
FROM python:3.12.0-slim

LABEL org.opencontainers.image.source=https://github.com/tp-maalsi23/citation-api

# Set the working directory to /app
WORKDIR /app

# Copy the current directory and file contents into the container at /app
COPY ./citation-api/ ./.env ./requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV APP_ENV=prod

# Run app.py when the container launches
CMD ["python", "/app/api.py"]
