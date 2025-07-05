# Run commands via `make <target>`
install:
	uv pip install -e .

run:
	python main.py

format:
	ruff format .

lint:
	ruff .

deploy:
	echo "Deployment script here"