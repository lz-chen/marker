# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the necessary files for installing dependencies
COPY pyproject.toml /app/

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code
COPY . /app

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the application as a service
CMD ["python", "run_marker_app.py"]
