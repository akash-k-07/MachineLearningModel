# Use a Python base image
FROM python:3.7-slim

# Install Rasa and its dependencies
RUN python -m pip install rasa

# Set the working directory in the container
WORKDIR /app

# Copy the local Rasa project directory to the container
COPY . /app/

# Make the start_services.sh script executable
RUN rasa train nlu

USER 1001

# Set the command to run your Rasa server with CORS
CMD ["run", "--enable-api", "--port", "8080", "--cors", "*"]
