# Intermediate image for building the optimizer
FROM python:3.6 as building_optimizer

LABEL stage=building_optimizer

ARG SSH_PRIVATE_KEY

RUN mkdir -p /root/.ssh/ && \
    echo "$SSH_PRIVATE_KEY" > /root/.ssh/id_rsa && \
    chmod -R 600 /root/.ssh/ && \
    ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

RUN echo "cloning private repo"

RUN git clone git@github.com:taoufik07/ensat-framework.git ./ensat_framework2

RUN echo "Hello from intermediate" > /intermediate_hello

# Base image
FROM python:3.6

# we install cython
RUN pip install cython

COPY . /app

WORKDIR /app

# we compile it
RUN python compile.py build_ext --inplace

# we remove `.py` and `.c`
RUN rm my_precious.py my_precious.c compile.py

RUN rm Dockerfile
RUN mv DockerfileRun Dockerfile

COPY --from=building_optimizer /intermediate_hello /

RUN cat /intermediate_hello

# we use it
CMD ["python", "main.py"]
