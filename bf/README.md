Re-creation of bf at https://morepypy.blogspot.com/2011/04/tutorial-writing-interpreter-with-pypy.html and https://github.com/disjukr/pypy-tutorial-ko

## Running with a Python interpreter outside a container
1. Run `setup_dev.sh` if this is the first time you are running this.
2. Run `PYTHONPATH=pypy <pypy | python2> main.py <.b source file>`

## Build with container
You can rebuild or manually copy the .b program whenever you make changes.

```sh
podman build -t bf ./
```

You can also use the Makefile provided to build the interpreter with JIT or without JIT
```sh
make jit     # Build with JIT
make no-jit  # Build without JIT
```

## Running the container
Make sure the .b program you provided is in the container

```sh
podman run -it --rm --name bf <bf | bf-nojit> <.b file>
```

For example, running with JIT:
```sh
podman run -it --rm --name bf bf mandel.b
```
