import sys
from grammar import grammar
from limit_fuzzer import LimitFuzzer_NR


def entry_point(argv):
    fuzzer = LimitFuzzer_NR(grammar)
    print(fuzzer.fuzz())
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
