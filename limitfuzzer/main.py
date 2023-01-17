import sys
from grammar import grammar
from limit_fuzzer_rpy import LimitFuzzer_NR, LimitFuzzer
from utils import write_bytes_to_stdout, print_


def entry_point(argv):
    fuzzer = LimitFuzzer_NR(grammar)
    fuzz_result = fuzzer.fuzz()
    write_bytes_to_stdout(fuzz_result)
    # print_(fuzz_result, end="")
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
