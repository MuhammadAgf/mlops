PHONY: clean install build run_image


GIT_DIGEST := $(shell git rev-parse --short HEAD)

clean:
	find . | grep -E "(__pycache__|\.pyc|\.lprof)" | xargs rm -rf

install:
	pip install -r requirements.txt


build: clean
	docker build -t ${DOCKER_USER}/mlops-demo-be:$(GIT_DIGEST) -t ${DOCKER_USER}/mlops-demo-be:latest -f Dockerfile .

build_local: clean
	docker build -t mlops-demo-be -f Dockerfile .


run_image:
	docker run -it --rm mlops-demo-be
