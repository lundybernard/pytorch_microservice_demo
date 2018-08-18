# pytorch_microservice_demo
demonstrate a dockerized microservice that uses pytorch with CUDA acceleration

## Requirements
### System
[docker-ce v18.06.0-ce +](https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/#uninstall-old-versions)
[nvidia-docker2](https://github.com/NVIDIA/nvidia-docker)

### Conda packages
pytorch


## Dev notes
pip install docker-compose (not in conda repositories)

### TODO:
create performance tests, and figure out how to perf-test differences between versions

Deploy to GCP, and verify GPU acceleration


## Installation
install in developer mode from source

```
python setup.py develop
```

## Run Integration tests

### Manually
start the web server manually

```
python pytorch_server/pytorch_server.py
```

run tests against the web server

```
python -m unittest integration_tests/service_test.py
pytest integration_tests/service_test.py
```

### Run the service and tests via CLI
Install the package

```
python setup.py install
python setup.py develop
```

start webserver with cli

```
pytorch_server start
```

Run functional tests

```
pytorch_cli test service
pytest integration_tests/service_test.py
```

### Run Container tests
to validate the docker container works properly, and docker-compose works

#### Manual Test
Run the container with docker-compose and test it with service_testf

```
docker-compose build
docker-compose up
pytest integraiton_tests/service_test.py
```

#### Automatic test
container_test will run docker-compose before each test case,
and execute the test against the running container

```
python -m unittest integraiton_tests/container_test.py
pytest integraiton_tests/container_test.py
```


## rebuild local containers
sometimes necessary if container tests are failing
```
docker-compose down --rmi local
docker-compose build
```
