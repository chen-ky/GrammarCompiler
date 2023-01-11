import os


STDOUT_FD = 1
STDERR_FD = 2


def print_(string, end="\n"):
    os.write(STDOUT_FD, ("%s%s" % (string, end)))


def println(string):
    print_(string, "\n")


def eprint(string, end="\n"):
    os.write(STDERR_FD, ("%s%s" % (string, end)))


def eprintln(string):
    eprint(string, "\n")