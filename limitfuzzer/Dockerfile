FROM docker.io/library/fedora:latest

RUN dnf update -y \
    && dnf install -y gcc python2 pypy mercurial bzip2

RUN useradd -m -U user

WORKDIR "/home/user"
USER user:user

RUN hg clone https://foss.heptapod.net/pypy/pypy
COPY --chown=user:user utils ./utils
COPY --chown=user:user *.json *.py ./

RUN PYTHONPATH=pypy pypy ./pypy/rpython/bin/rpython --output limit-fuzzer main.py

ENTRYPOINT ["/home/user/limit-fuzzer"]
