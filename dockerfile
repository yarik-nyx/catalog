FROM python:3.11-slim

RUN pip install poetry==2.1.3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app_api
COPY pyproject.toml ./
RUN poetry install --no-root

COPY . .



