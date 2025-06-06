# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make sure the models directory exists
RUN mkdir -p models

# Create a non-root user
RUN adduser --disabled-password --gecos '' api_user
RUN chown -R api_user:api_user /app
USER api_user

# Command to run the application
CMD uvicorn api.main:app --host 0.0.0.0 --port $PORT 