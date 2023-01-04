PHONY: clean install build run_image


GIT_DIGEST := $(shell git rev-parse --short HEAD)

clean:
	find . | grep -E "(__pycache__|\.pyc|\.lprof)" | xargs rm -rf

install:
	pip install -r requirements.txt


build: clean
	docker build -t ${DOCKER_USER}/mlops-demo-sa-be:$(GIT_DIGEST) -t ${DOCKER_USER}/mlops-demo-sa-be:latest -f Dockerfile .

run_image:
	docker run -it --rm ${DOCKER_USER}/mlops-demo-sa-be
