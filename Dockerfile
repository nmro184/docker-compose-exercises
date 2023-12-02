# Use the official Python image
FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY requirements.txt .
COPY main.py .
COPY templates templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "main.py"]
