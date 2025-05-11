FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create logs and data directories
RUN mkdir -p /app/logs /app/data

# Copy project files
COPY . .

# Set working directory where scrapy.cfg is located
WORKDIR /app

# Run the command
CMD ["scrapy", "crawl", "spacenets_spider"]