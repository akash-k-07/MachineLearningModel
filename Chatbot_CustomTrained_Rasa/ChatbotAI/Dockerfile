# Use a Python base image
FROM python:3.7-slim

# Install Rasa and its dependencies
RUN python -m pip install rasa


# Set the working directory in the container
WORKDIR /app

# Copy the local Rasa project directory to the container
COPY ..

# Make the start_services.sh script executable
RUN rasa train nlu

USER 1001

ENTRYPOINT ["rasa"]

# Set the command to run your start_services.sh script
CMD ["run","--enable-api","--port","8080"]
