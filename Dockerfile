FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg2 chromium chromium-driver

RUN pip install selenium

ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="$PATH:/usr/lib/chromium/"

WORKDIR /app
COPY test/test_webapp.py .

CMD ["python", "test_webapp.py"]
