# Use a base image with Python
FROM python:3.11-slim

# Set the working directory
WORKDIR /fastapi-app

# Copy the current directory into the container
COPY . /fastapi-app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the fastapi runs on
EXPOSE 80

# CMD Pipeline running the server
CMD ["uvicorn", "fastapi-app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]