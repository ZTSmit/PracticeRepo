# Use an official Python runtime as a parent image
FROM python:3.13-slim-trixie

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django project into the container
COPY . /app/

# Expose the port your Django app will run on (e.g., 8000)
EXPOSE 8000

# Define the command to run your Django application
# <!> Do not runserver in a real production environment, use gunicorn  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]