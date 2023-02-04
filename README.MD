MLOPS with Kubernetes 0 to 1 
==============================
**this repository assume that you have basic knowledge on Docker and Python and intended for learning purposes**

## Prerequisite
1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/)
2. Create a [Dockerhub](https://hub.docker.com/) account (or any container registry)
3. install [kubectl](https://kubernetes.io/docs/tasks/tools/) and minikube if you want to run this locally
4. install [istio](https://istio.io/latest/docs/setup/getting-started/) (for the gateway)
5. (for Scheduling with Airflow) install [helm](https://helm.sh/docs/intro/install/)

## Setup
1. basic setup <#TODO-link>
2. create model server and setup deployment with mlserver in kubernetes <#TODO-link>
3. setup and create scheduler with airflow <#TODO-link>

## Directory Structure
the directory structured such that:
1. `manifest` contain all kubernetes configuration file, with the deployment config for each services put in the `manifest/<service-folder>/` mirroring `services/<service-folder>`
2. `services` contain all services code, in this case 
    * `sa-be` to simulate the backend service that will call our ML service
    * `sa-ml` the machine learning service deployed using mlserver
    * `ml-helper` helper image to load model from GCS to our ml service (explained in X)
3. `trainer` contain the training pipeline to be used by the airflow dags

outside this repository: a [repo](https://github.com/MuhammadAgf/airflow-dags) for the airflow dags

## Tutorial

### Deployment
to deploy a service you can execute `make deploy svc=<service-folder> ns=<namespace>`
for example:  `make deploy svc=sa-ml ns=demo`

### Scheduling Training Pipeline
1. the repository for the dags is [here](https://github.com/MuhammadAgf/airflow-dags)
2. go to `trainer` to see the directory that store the training pipeline example

### [coming soon] Tracking with MLFlow
coming soon. . .

### [coming soon] CI/CD
coming soon. . .

```
├── Makefile #contain make deploy command
├── manifest #kubernetes configuration
│   ├── airflow
│   │   └── rbac.yaml
│   ├── istio
│   │   ├── http-gateway.yaml
│   │   └── vs-route-ingress.yaml
│   ├── sa-be
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── sa-ml
│       ├── deployment.yaml
│       └── service.yaml
├── README.MD
├── services  
│   ├── ml-helper
│   │   ├── Dockerfile
│   │   └── start.sh
│   ├── sa-be
│   │   ├── app
│   │   │   └── main.py
│   │   ├── Dockerfile
│   │   ├── Makefile
│   │   └── requirements.txt
│   └── sa-ml
│       ├── Dockerfile
│       ├── Makefile
│       ├── models
│       ├── model-settings.json
│       └── requirements.txt
└── trainer
    └── text-trainer
        ├── Dockerfile
        ├── Makefile
        ├── requirements.txt
        └── worker
            ├── gcs.py
            └── main.py
```

## from 1 to hero
<list of learning resources to deepen understanding>


### More References

1. https://github.com/4OH4/kubernetes-fastapi
2. https://github.com/rinormaloku/k8s-mastery/
3. https://rinormaloku.com/series/kubernetes-and-everything-else/

