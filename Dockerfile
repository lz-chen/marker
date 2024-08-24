# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and create a swap file
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && \
    fallocate -l 1G /swapfile && \
    chmod 600 /swapfile && \
    mkswap /swapfile && \
    swapon /swapfile

# Install Poetry globally
RUN pip install poetry

# Copy only the necessary files for installing dependencies
COPY pyproject.toml /app/

# Install dependencies globally
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code
COPY . /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the application as a service
CMD ["python", "run_marker_app.py"]
