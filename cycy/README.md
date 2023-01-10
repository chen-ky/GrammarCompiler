https://building-an-interpreter-with-rpython.readthedocs.io/en/latest/02-CyCy.html
https://github.com/DeloitteHux/cycy

`podman build -t cycy ./`
`podman run -it --rm -t --name cycy cycy`
---
`cd bin`
`./cycy-nojit`
`int main(void) { return 0; }`
