#Usee the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and Redis client
RUN pip install --no-cache-dir flask redis

# Expose port 5000 (the port Flask will run on)
EXPOSE 5000

# Set the environment variable for the Redis host (default is 'redis')
ENV REDIS_HOST redis
ENV REDIS_PORT 6379

# Command to run the application
CMD ["python", "app.py"]