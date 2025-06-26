FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set display (optional)
ENV DISPLAY=:99

# Set work directory
WORKDIR /app

# Copy everything
COPY . .

# Install Python libs
RUN pip install -r requirements.txt

# Run the test
CMD ["python", "-m", "unittest", "test_webapp.py"]
