# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt first
COPY requirements.txt .

# Install required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your application files
COPY . .

# Make the run_services.sh script executable
RUN chmod +x bin/run_services.sh

# Expose the ports for Prefect and Uvicorn
EXPOSE 4201 8001

# Run the services
CMD ["bin/run_services.sh"]
