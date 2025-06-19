# Use Python base image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium

# Set display environment (for headless browser testing)
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="/usr/lib/chromium:$PATH"

# Set workdir
WORKDIR /app

# Copy code files
COPY ./code /app

# Install Python packages
RUN pip install selenium

# Default command (optional, for deployment)
CMD ["python3", "-m", "http.server", "8000"]
