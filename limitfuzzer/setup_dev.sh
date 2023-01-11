#!/bin/sh

# Quit on failure
set -e


check_python() {
    if $(hash pypy &> /dev/null)
    then
        USE_PY='pypy'
    elif $(hash python2 &> /dev/null)
    then
        USE_PY='python2'
    else
        echo "No suitable python2 installation found. Please install python2 or pypy."
        return 1
    fi
    return 0
}

hg_clone_pypy() {
    hg clone 'https://foss.heptapod.net/pypy/pypy'
}

main() {
    check_python
    hg_clone_pypy
    echo "Done! Remember to run with `PYTHONPATH=pypy <pypy or python2> <main.py>` so we can use rpython toolchain"
}


main
