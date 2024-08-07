FROM python:3.10

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app
