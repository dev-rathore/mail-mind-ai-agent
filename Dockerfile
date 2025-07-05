# Build image with: docker build -t email-agent .
# Run container: docker run --env-file .env email-agent
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install uv && \
    uv pip install -e .

CMD ["python", "main.py"]
