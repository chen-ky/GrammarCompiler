import sys
from grammar import grammar
from limit_fuzzer_rpy import LimitFuzzer_NR, LimitFuzzer
from utils import write_bytes_to_stdout, print_


def entry_point(argv):
    rand_from_std_in = False
    # recursive_fuzzer = False
    for v in argv:
        if v == "--stdin-rand":
            rand_from_std_in = True
        # if v == "--recursive":
        #     recursive_fuzzer = True
    # if recursive_fuzzer:
    #     fuzzer = LimitFuzzer(grammar, rand_from_stdin=rand_from_std_in)
    # else:
    fuzzer = LimitFuzzer_NR(grammar, rand_from_stdin=rand_from_std_in)
    fuzz_result = fuzzer.fuzz()
    write_bytes_to_stdout(fuzz_result)
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
