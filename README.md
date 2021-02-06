# ml-k8s-prod
Machine Learning with Kubernetes

## Docker Build
```sh
$ docker-compose build
```

## [Optional] Run jupyter notebooks
```sh
$ docker run -v $(pwd):/code/ -p 5000:5000 -it titanic:dev bash
```

```sh
$ jupyter notebook --allow-root --ip=0.0.0.0 --port 5000
```

- notebooks:
    -  Titanic.ipynb


## Train Model & Exposed into an API.
```sh
$ docker-compose up
```

### Request example
```python
import requests
url = 'http://0.0.0.0:5000/predict'
data = {"sex": "male", "pclass": 2}
resp = requests.get(url, json=data)
print(resp.json())
```


## K8s with local image.
```sh
$ minikube start
```
```sh
$ eval $(minikube docker-env)
```
```sh
$ docker-compose build
```
```sh
$ kubectl apply -f deployment.yaml
```
```sh
$ kubectl apply -f service.yaml
```

```python
# find ip in minikube docker container. (ip a)
# find port in k8s service.
import requests
url = 'http://<container_minikube_ip>:<k8s_service_port>/predict'
data = {"sex": "male", "pclass": 2}
resp = requests.get(url, json=data)
print(resp.json())
```