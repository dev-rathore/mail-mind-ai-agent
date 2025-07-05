# Build with: docker build -t mail-mind-ai-agent .
# Run with: docker run --env-file .env mail-mind-ai-agent

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies using uv
RUN pip install uv && \
    uv pip install -e .

# Use CLI entrypoint from pyproject.toml
CMD ["python", "app/main.py"]
