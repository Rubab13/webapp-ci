FROM python:3.10-slim

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 gnupg lsb-release xz-utils \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver

# Install Python packages
RUN pip install selenium

# Copy app files
COPY . /app
WORKDIR /app

# Expose port 5500
EXPOSE 5500

# Start web server in background, wait, and run test
CMD python3 -m http.server 5500 & \
    sleep 2 && \
    python3 test.py
