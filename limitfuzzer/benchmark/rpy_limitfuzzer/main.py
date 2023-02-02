import sys
from grammar import grammar
from limit_fuzzer_rpy import LimitFuzzer_NR, LimitFuzzer
from utils import write_bytes_to_stdout, print_, eprintln
from timeit import default_timer as timer


def entry_point(argv):
    rand_from_std_in = False
    is_benchmark = False
    runs = 1
    # recursive_fuzzer = False
    skip_next = False
    for i, v in enumerate(argv):
        if skip_next:
            skip_next = False
            continue
        arg = v.split("=", 1)
        if arg[0] == "--stdin-rand":
            rand_from_std_in = True
        elif arg[0] == "--runs":
            if len(arg) < 2:
                if i + 1 < len(argv):
                    runs = int(argv[i + 1])
                    skip_next = True
                else:
                    eprintln("Please specify the number of runs.")
                    return 1
            else:
                runs = int(arg[1])
        elif arg[0] == "--benchmark":
            is_benchmark = True
        # elif v == "--recursive":
        #     recursive_fuzzer = True

    if runs <= 0:
        eprintln("Runs must be larger than 0.")
        return 1

    start_time = 0.0

    if is_benchmark:
        start_time = timer()
    # if recursive_fuzzer:
    # else:
    # fuzzer = LimitFuzzer(grammar, rand_from_stdin=rand_from_std_in)
    fuzzer = LimitFuzzer_NR(grammar, rand_from_stdin=rand_from_std_in)
    while runs > 0:
        fuzz_result = fuzzer.fuzz()
        write_bytes_to_stdout(fuzz_result)
        runs -= 1
    if is_benchmark:
        end_time = timer()
        print_("\nRuntime: %f seconds" % (end_time - start_time))
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
