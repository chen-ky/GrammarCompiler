FROM docker.io/library/fedora:latest

RUN dnf update -y \
    && dnf install -y gcc python2 pypy mercurial

# RUN useradd -m -U user

# WORKDIR "/home/user"
WORKDIR "/"
# USER user:user

RUN hg clone https://foss.heptapod.net/pypy/pypy
COPY ./*.py grammar.txt ./example-interpreter
COPY ./test ./example-interpreter

WORKDIR "/example-interpreter"
RUN PYTHONPATH=../pypy pypy ../pypy/rpython/bin/rpython targetkermit.py
COPY ./samples ./example-interpreter

ENTRYPOINT ["bash"]
