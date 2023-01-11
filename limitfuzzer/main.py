import sys
from grammar import grammar
from limit_fuzzer_rpy import LimitFuzzer
from utils import print_
from utils.random import RRandom


def entry_point(argv):
    fuzzer = LimitFuzzer(grammar)
    print_(fuzzer.fuzz(), end="")
    # print(fuzzer.fuzz())
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
