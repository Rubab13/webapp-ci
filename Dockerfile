# FROM nginx:alpine
# COPY . /usr/share/nginx/html

# Use official Python base image
FROM python:3.10-slim

# Install Chrome and dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set display port to avoid errors
ENV DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Run test command by default (optional)
CMD ["python", "-m", "unittest", "web_test.py"]
