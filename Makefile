setup-istio:
	istioctl install --set profile=demo -y
	kubectl label namespace demo istio-injection=enabled

apply-istio:
	kubectl apply -f manifest/istio -n demo


redeploy:
	kubectl rollout restart deployment/$(svc) -n $(ns)
	kubectl rollout status deployment $(svc) -n $(ns)


build-deploy:
	cd services/$(svc) && make build
	docker push ${DOCKER_USER}/mlops-demo-$(svc):latest
	cd ../..
	kubectl apply -f manifest/$(svc) -n $(ns)
	kubectl rollout status deployment $(svc) -n $(ns)

deploy:
	kubectl apply -f manifest/$(svc) -n $(ns)
	kubectl rollout status deployment $(svc) -n $(ns)
