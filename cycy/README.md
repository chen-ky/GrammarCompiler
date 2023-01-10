## Steps
### Building and running container

1. `podman build -t cycy ./`
2. `podman run -it --rm -t --name cycy cycy`

### Running cycy interpreter

1. `cd bin`
2. `./cycy-nojit`
3. `int main(void) { return 0; }`

## References

* Source code: https://github.com/DeloitteHux/cycy
* https://building-an-interpreter-with-rpython.readthedocs.io/en/latest/02-CyCy.html
