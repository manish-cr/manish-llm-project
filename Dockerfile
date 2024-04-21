# Use an official Python runtime as a base image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire current directory into the container
COPY . .

# Install dotenv library for loading environment variables from .env file
RUN pip install python-dotenv

# Command to run the chatbot script
CMD ["python", "src/my_first_llm_app.py"]
