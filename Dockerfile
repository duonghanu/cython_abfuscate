FROM python:3.6

# we install cython
RUN pip install cython

COPY . /app

WORKDIR /app

# we compile it
RUN python compile.py build_ext --inplace

# we remove `.py` and `.c`
RUN rm my_precious.py my_precious.c compile.py

# we use it
CMD ["python", "main.py"]





