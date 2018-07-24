FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

RUN python -m unittest discover pytorch_server.tests -p '*_test.py'

CMD ["python", "pytorch_server/pytorch_server.py"]
