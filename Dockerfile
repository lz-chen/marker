# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

# Install Poetry and Gunicorn globally
RUN pip install poetry gunicorn

# Copy only the necessary files for installing dependencies
COPY pyproject.toml /app/

# Install dependencies globally
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code
COPY . /app

# Make port 8501 available to the world outside this container
EXPOSE 8000

# Run the application using Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "--timeout", "300", "run_marker_app:app"]
