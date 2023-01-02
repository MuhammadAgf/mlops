PHONY: clean install build run_image

clean:
	find . | grep -E "(__pycache__|\.pyc|\.lprof)" | xargs rm -rf

install:
	pip install -r requirements.txt

build_local: clean
	docker build -t mlops-demo-be -f Dockerfile .


run_image:
	docker run -it --rm mlops-demo-be
