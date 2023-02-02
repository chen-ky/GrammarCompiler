from fuzzer import CFuzzer, CTrans
from grammar import grammar


if "__main__" == __name__:
    fuzzer_generator = CFuzzer(CTrans(grammar).translate())
    main_src, fuzz_src = fuzzer_generator.fuzz_src()
    print(fuzz_src)
    print(main_src)
