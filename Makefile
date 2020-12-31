NAME ?= rokcarl/derby-benchmark

all: build

build:
	docker build -t $(NAME) .

push:
	docker push $(NAME)

python:
	docker run --network host -it $(NAME) python

shell:
	docker run --network host -it $(NAME) bash

run:
	@echo "Run the application using 'docker run --network host $(NAME) /app/run.py -h'"
