import sys
from grammar import grammar
from limit_fuzzer_rpy import LimitFuzzer_NR, LimitFuzzer
from utils import print_


def entry_point(argv):
    fuzzer = LimitFuzzer(grammar)
    print_(fuzzer.fuzz(), end="")
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
