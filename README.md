# pytorch_microservice_demo

## Requirements
### System
docker-ce
nvidia-docker

### Conda packages
docker-compose


## Dev notes
pip install docker-compose (not in conda repositories)

## Run Integration tests

rebuild local containers
```
docker-compose down --rmi local
docker-compose build
```
