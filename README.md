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

## Run Integration tests

rebuild local containers
```
docker-compose down --rmi local
docker-compose build
```
