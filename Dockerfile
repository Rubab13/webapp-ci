# # Use official Nginx image
# FROM nginx:alpine

# # Remove default nginx content
# RUN rm -rf /usr/share/nginx/html/*

# # Copy your static web files to Nginx
# COPY . /usr/share/nginx/html

# # Expose port 80
# EXPOSE 80

FROM python:3.10-slim

# Install Chrome dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg libnss3 libgconf-2-4 libxi6 libxcomposite1 libxcursor1 libxdamage1 \
    libxrandr2 libxtst6 libatk1.0-0 libatk-bridge2.0-0 libcups2 libgbm1 libgtk-3-0 xvfb fonts-liberation

# Install Chrome browser
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

# Set environment variables
ENV CHROME_BIN=/usr/bin/google-chrome \
    CHROMEDRIVER=/usr/local/bin/chromedriver \
    DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test code
COPY . .

# Run headless tests
CMD ["pytest", "--maxfail=1", "--disable-warnings", "--html=report.html", "test/test_cases.py"]
