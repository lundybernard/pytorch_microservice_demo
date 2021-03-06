FROM nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

# Update OS
RUN apt-get update && apt-get install -y --no-install-recommends \
         curl \
         &&\
     rm -rf /var/lib/apt/lists/*

# Install Conda
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda install pytorch && \
     /opt/conda/bin/conda clean -ya
ENV PATH /opt/conda/bin:$PATH


# This must be done before pip so that requirements.txt is available
ADD . /src
WORKDIR /src

RUN pip install -r requirements.txt

# Run unittests, fails the build on failing tests
# WARNING! cuda is not available durring the build process
# Tests must work without cuda, or be disabled when cuda is unavailable.
RUN python -m unittest discover pytorch_server.tests -p '*_test.py'

RUN python setup.py develop
#CMD ["python", "pytorch_server/pytorch_server.py"]
CMD ["pytorch_server", "start"]
