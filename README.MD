MLOPS with Kubernetes 0 to 1
==============================
**this repository assume that you have basic knowledge on Docker and Python and intended for learning purposes**

## Prerequisite
1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/)
2. Create a [Dockerhub](https://hub.docker.com/) account (or any container registry)
3. install [kubectl](https://kubernetes.io/docs/tasks/tools/)
4. install [istioctl](https://istio.io/latest/docs/reference/commands/istioctl/) (for the gateway)
5. (for Scheduling with Airflow) install [helm](https://helm.sh/docs/intro/install/)
6. for local development you can install [Minikube](https://minikube.sigs.k8s.io/docs/start/)
7. Google Cloud Storage account (for `trainer` to push model to gcs and `ml-helper` to load model from gcs)

## Setup
1. set `DOCKER_USER` environment variable for image registry target (in my case `m46f`)
2. update all the `image` user in the `manifest` to the value of the `DOCKER_USER` specified above (for example if your user is `alice`)
    from:
    ```
    manifest/sa-ml/deployment.yaml:31:          image: m46f/mlops-demo-ml-helper:latest
    manifest/sa-ml/deployment.yaml:49:          image: m46f/mlops-demo-sa-ml:latest
    manifest/sa-be/deployment.yaml:24:        - image: m46f/mlops-demo-sa-be:latest
    ```
    to:
    ```
    manifest/sa-ml/deployment.yaml:31:          image: alice/mlops-demo-ml-helper:latest
    manifest/sa-ml/deployment.yaml:49:          image: alice/mlops-demo-sa-ml:latest
    manifest/sa-be/deployment.yaml:24:        - image: alice/mlops-demo-sa-be:latest
    ```
3. upload `model_chace/text-clf.joblib` to your storage (for this example we use google storage) and update the value inside `manifest/sa-ml/deployment.yaml:41:` from `"gs://morgana-mlops/demo/text-clf.joblib"` to your GCS path
4. have a kubernetes cluster running
5. create a `demo` namespace using `kubectl create namespace demo`
6. assuming you have a secret for GCS, create a secret for `GOOGLE_APPLICATION_CREDENTIALS` using `kubectl create secret -n demo generic google-app-key --from-file=secret.json=<path-to-your-secret-file.json>`
    this will store your secret as `google-app-key` secret inside the kubernetes `demo` namespace
    it will be accessed by `sa-ml` svc defined in
    ```
          volumeMounts:
            - name: model-volume
              mountPath: "/models"
            - name: google-cloud-keys
              mountPath: /var/secrets/google
              readOnly: true
          env:
            - name: GOOGLE_APPLICATION_CREDENTIALS
              value: /var/secrets/google/secret.json
    ```
7. setup istio https://istio.io/latest/docs/setup/install/istioctl/ (or you can use `make setup-istio` for quick setup including setting the istio-injection for `demo` namespace)
8. apply the istio manifest using `make apply-istio`


## Directory Structure
the directory structured such that:
1. `manifest` contain all kubernetes configuration file, with the deployment config for each services put in the `manifest/<service-folder>/` mirroring `services/<service-folder>`
2. `services` contain all services code, in this case 
    * `sa-be` to simulate the backend service that will call our ML service
    * `sa-ml` the machine learning service deployed using mlserver
    * `ml-helper` helper image to load model from GCS to our ml service
3. `trainer` contain the training pipeline to be used by the airflow dags

outside this repository: a [repo](https://github.com/MuhammadAgf/airflow-dags) for the airflow dags

```
├── Makefile #contain helper command
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

## Tutorial

### Build Image
to build an Image you can use `make build svc=<service-folder>` for example `make build svc=sa-ml`

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


## from 1 to hero
<list of learning resources to deepen understanding>


### References

1. https://github.com/4OH4/kubernetes-fastapi
2. https://github.com/rinormaloku/k8s-mastery/
3. https://rinormaloku.com/series/kubernetes-and-everything-else/

