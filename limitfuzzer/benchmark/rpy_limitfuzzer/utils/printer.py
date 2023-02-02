import os


STDOUT_FD = 1
STDERR_FD = 2


def print_(string, end="\n"):
    to_print = string + end
    os.write(STDOUT_FD, to_print)


def println(string):
    print_(string, "\n")


def write_bytes_to_stdout(bytearr):
    os.write(STDOUT_FD, bytearr)


def eprint(string, end="\n"):
    to_print = string + end
    os.write(STDERR_FD, to_print)


def eprintln(string):
    eprint(string, "\n")