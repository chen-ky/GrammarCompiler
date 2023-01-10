FROM docker.io/library/fedora:latest

RUN dnf update -y \
    && dnf install -y gcc python2 pypy git bzip2

RUN useradd -m -U user

WORKDIR "/home/user"
USER user:user

RUN curl https://foss.heptapod.net/pypy/pypy/-/archive/branch/default/pypy-branch-default.tar.bz2 | tar -xjf -
RUN git clone https://github.com/DeloitteHux/cycy.git

WORKDIR "/home/user/cycy"
RUN pypy -m ensurepip
RUN pypy -m pip install -e .
RUN pypy ../pypy-branch-default/rpython/bin/rpython cycy/target.py
RUN mkdir bin && mv target-c bin/cycy-nojit
ENTRYPOINT ["bash"]
