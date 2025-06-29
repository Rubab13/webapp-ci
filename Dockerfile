FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium chromium-driver python3-pip curl unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install selenium

ENV PATH="/usr/lib/chromium/:$PATH"
ENV CHROME_BIN="/usr/bin/chromium"

WORKDIR /app

COPY . .

CMD python3 -m http.server 8000 &
CMD ["python3", "./tests/test_cases.py"]
