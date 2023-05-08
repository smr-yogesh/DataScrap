FROM python:3.9-slim-buster

# Install required packages for pyppeteer for scraping.
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
    git \
    curl \
    gnupg \
    wget \
    bzip2 \
    libfontconfig \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5050

CMD ["python", "app.py" ]