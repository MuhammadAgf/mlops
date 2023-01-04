
deploy:
	cd services/$(svc) && make build
	docker push ${DOCKER_USER}/mlops-demo-$(svc):latest
	cd ../..
	kubectl apply -f manifest/$(svc)/deployment.yaml -n $(ns)
	kubectl rollout status deployment $(svc) -n $(ns)
