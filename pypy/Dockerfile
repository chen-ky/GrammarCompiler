FROM docker.io/library/fedora:latest

RUN dnf update -y \
    && dnf install -y gcc python2 pypy mercurial

RUN useradd -m -U user

WORKDIR "/home/user"
USER user:user

RUN hg clone https://foss.heptapod.net/pypy/pypy
COPY *.json *.py ./

RUN pypy pypy/rpython/bin/rpython grammar_compiler_rpy.py

ENTRYPOINT ["/home/user/grammar_compiler_rpy-c"]
