# Use Ubuntu 18.04 as the base image
FROM ubuntu:18.04

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Rasa and its dependencies
RUN python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==1.10.8 --use-feature=2020-resolver

# Copy the local Rasa project directory to the container
COPY . /app/

# Make the start_services.sh script executable
RUN chmod +x /app/start_services.sh

# Set the command to run your start_services.sh script
CMD ["/app/start_services.sh"]
