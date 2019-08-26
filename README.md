# Clone the repo

    git clone git@github.com:taoufik07/cython_abfuscate.git

# Build
    docker build -t ob_test .

# Run
    docker run ob_test

#

Obfuscate with cython (and a bonus ~3x speed) withouth touching the existing code


In a nutshell, this is the idea, Cython "compiles" python code to C files `.c` then generate `.so` that will shipped to the client


This docker container takes an app with clear code then generates a new one with obfuscated code, that will be sent to the client.


In this example I've "obfuscated" `my_precious.py`


# Inspect locally

You can copy and inspect the result files locally

First build

    docker build -t ob_test .

Then copy the files

    sudo docker cp $(docker run -i -d ob_test):/app . 

And locally you will find the `app` directory
