# Run commands via `make <target>`

install:
	uv pip install -e .

run:
	python app/main.py

cli:
	mail-mind-ai-agent

format:
	ruff format .

lint:
	ruff check .

docker-build:
	docker build -t mail-mind-ai-agent .

docker-run:
	docker run --env-file .env mail-mind-ai-agent

deploy:
	echo "Add deployment script here"
