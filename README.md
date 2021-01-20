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