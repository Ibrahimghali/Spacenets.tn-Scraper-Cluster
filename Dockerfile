FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Use environment variables for configuration
ENV PYTHONPATH=/app
ENV SCRAPY_SETTINGS_MODULE=spacenets.settings

CMD ["scrapy", "crawl", "spacenets_spider"]