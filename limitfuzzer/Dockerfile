FROM docker.io/library/fedora:latest

RUN dnf update -y \
    && dnf install -y gcc python2 pypy mercurial bzip2

RUN useradd -m -U user

WORKDIR "/home/user"
USER user:user

RUN hg clone https://foss.heptapod.net/pypy/pypy
COPY utils ./utils
COPY *.json *.py ./

RUN PYTHONPATH=pypy pypy ./pypy/rpython/bin/rpython main.py

ENTRYPOINT ["/home/user/main-c"]
