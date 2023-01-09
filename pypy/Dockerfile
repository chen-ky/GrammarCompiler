FROM docker.io/library/fedora:latest

RUN dnf update -y \
    && dnf install -y gcc python2 pypy git bzip2

RUN useradd -m -U user

WORKDIR "/home/user"
USER user:user

RUN curl https://foss.heptapod.net/pypy/pypy/-/archive/branch/default/pypy-branch-default.tar.bz2 | tar -xjf -
COPY *.json *.py ./

RUN pypy pypy-branch-default/rpython/bin/rpython grammar_compiler_rpy.py

ENTRYPOINT ["/home/user/grammar_compiler_rpy-c"]
