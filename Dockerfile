# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install PyMySQL


# Copy the application code
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
