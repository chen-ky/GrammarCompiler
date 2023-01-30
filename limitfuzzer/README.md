Original source code: https://github.com/vrthra/F1/blob/061d39a/F1/fuzzer.py#L77

## Versions:
* `main_p3.py` is the original source code (in `limit_fuzzer.py`) with some code to start the program.
* `main.py` is the Python2 / RPython translation of the original source code.

Both versions share the `grammar.py` file for grammar definition.

## Running

### Flags
* `--stdin-read` read bytes from stdin as random source. Defaults to using a PRNG implementation if this flag is not specified.

### Python interpreter
For the Python3 version just run it like any other Python program: `python main_p3.py`

For the Python2 / RPython version:
1. If you haven't run `setup_dev.sh` before, run this script to download the rpython toolchain.
2. After that, if you want to run this using a Python2 interpreter, run `PYTHONPATH=pypy python2 main.py`.

### RPython
1. If you haven't run `setup_dev.sh` before, run this script to download the rpython toolchain.
2. Run `PYTHONPATH=pypy pypy ./pypy/rpython/bin/rpython main.py` to build with RPython.
3. Execute the binary: `./main-c`

#### Build and run in a container
1. Build the container with `podman build -t limit-fuzzer ./`
2. Run the container with `podman run -it --rm --name limit-fuzzer limit-fuzzer`
    * If you want provide the program with random bytes from stdin, run the program with the `--stdin-read` flag. `podman run -i --rm --name limit-fuzzer limit-fuzzer --stdin-read < /dev/urandom`

## Resources

* https://rpython.readthedocs.io/en/latest/rpython.html
* https://rpython.readthedocs.io/en/latest/rlib.html
