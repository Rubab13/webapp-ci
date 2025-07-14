# # Use official Nginx image
# FROM nginx:alpine

# # Remove default nginx content
# RUN rm -rf /usr/share/nginx/html/*

# # Copy your static web files to Nginx
# COPY . /usr/share/nginx/html

# # Expose port 80
# EXPOSE 80

# FROM python:3.10-slim

# # Install dependencies for Chrome + Selenium
# RUN apt-get update && apt-get install -y \
#     wget unzip curl gnupg libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libxss1 libappindicator3-1 libasound2 \
#     libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libxrandr2 \
#     chromium chromium-driver xvfb && \
#     rm -rf /var/lib/apt/lists/*

# # Set Chrome options
# ENV CHROME_BIN=/usr/bin/chromium \
#     CHROMEDRIVER=/usr/bin/chromedriver \
#     DISPLAY=:99

# # Set workdir
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy test files and web app
# COPY . .

# # Default command to run Selenium tests with Xvfb
# CMD Xvfb :99 -screen 0 1024x768x16 & pytest --html=report.html tests/test_cases.py

FROM python:3.10-slim

# Install system dependencies for Chrome, Xvfb, etc.
RUN apt-get update && apt-get install -y \
    gnupg2 curl wget unzip \
    xvfb \
    chromium chromium-driver \
    libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 \
    libxss1 libappindicator3-1 libasound2 \
    libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 \
    libxdamage1 libxi6 libxtst6 libxrandr2 \
    && rm -rf /var/lib/apt/lists/*

# Set Chrome and display env vars
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver
ENV DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Run tests using xvfb
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & pytest --html=report.html tests/test_cases.py"]
