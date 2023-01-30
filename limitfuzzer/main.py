import sys
from grammar import grammar
from limit_fuzzer_rpy import LimitFuzzer_NR, LimitFuzzer
from utils import write_bytes_to_stdout, print_, eprintln
from timeit import default_timer as timer


def entry_point(argv):
    rand_from_std_in = False
    benchmark_loop = 0
    # recursive_fuzzer = False
    skip_next = False
    for i, v in enumerate(argv):
        if skip_next:
            skip_next = False
            continue
        arg = v.split("=", 1)
        if arg[0] == "--stdin-rand":
            rand_from_std_in = True
        elif arg[0] == "--benchmark":
            if len(arg) < 2:
                if i + 1 < len(argv):
                    benchmark_loop = int(argv[i + 1])
                    skip_next = True
                else:
                    eprintln("Please specify benchmark loop count.")
                    return 1
            else:
                benchmark_loop = int(arg[1])
        # elif v == "--recursive":
        #     recursive_fuzzer = True
    start_time = 0.0
    runs = 1
    if benchmark_loop > 0:
        runs = benchmark_loop
        start_time = timer()
    elif benchmark_loop < 0:
        eprintln("Benchmark loop cannot be negative.")
        return 1
    else:
        print_("Warning: Benchmark loop is 0, not running benchmark.")
    # if recursive_fuzzer:
    #     fuzzer = LimitFuzzer(grammar, rand_from_stdin=rand_from_std_in)
    # else:
    fuzzer = LimitFuzzer_NR(grammar, rand_from_stdin=rand_from_std_in)
    while runs > 0:
        fuzz_result = fuzzer.fuzz()
        write_bytes_to_stdout(fuzz_result)
        runs -= 1
    if benchmark_loop > 0:
        end_time = timer()
        print_("Runtime: %f seconds" % (end_time - start_time))
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
