FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*
EXPOSE 5002
# Command to run the application
CMD ["python", "app.py"]
