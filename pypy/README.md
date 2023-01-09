* Grammar definition is in `grammar.py`
* Python 3 code is in `grammar_compiler.py`
* Python 2 code is in `grammar_compiler_py2.py`
* RPython code is in `grammar_compiler_rpy.py`

## Building and Running Container
1. `podman build -t pypy-g-compiler .`
2. `podman run -it --rm -t --name pypy-g-compiler pypy-g-compiler`
