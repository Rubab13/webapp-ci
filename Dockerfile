# FROM nginx:alpine
# COPY . /usr/share/nginx/html

FROM python:3.9

# Install Chrome
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg ca-certificates chromium chromium-driver \
    && apt-get clean

# Set path for Chrome and ChromeDriver
ENV PATH="/usr/lib/chromium/:$PATH"
ENV CHROME_BIN=/usr/bin/chromium

# Install Python packages
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copy source code
COPY . /app
