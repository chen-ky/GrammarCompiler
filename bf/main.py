import sys
import os
import rpython.rlib.streamio as streamio
from rpython.rlib.jit import JitDriver, purefunction


def get_location(pc, source_code, bracket_match):
    assert pc >= 0
    return "%s_%s_%s" % (
            source_code[:pc], source_code[pc], source_code[pc+1:]
            )


jitdriver = JitDriver(greens=["pc", "source_code", "bracket_match"], reds=["tape"], get_printable_location=get_location)
VALID_OPERATOR = [">", "<", "+", "-", "[", "]", ".", ","]
TAPE_DEFAULT_VAL = 0
STDIN_FD = 0
STDOUT_FD = 1
STDERR_FD = 2


class Tape(object):
    def __init__(self):
        self.tape = [TAPE_DEFAULT_VAL]
        self.ptr = 0

    def move_right(self):
        self.ptr += 1
        if len(self.tape) <= self.ptr:
            self.tape.append(TAPE_DEFAULT_VAL)

    def move_left(self):
        if self.ptr - 1 < 0:
            raise RuntimeError("Invalid instruction, tape pointer cannot be less than 0")
        self.ptr -= 1

    def inc(self):
        self.tape[self.ptr] += 1

    def dec(self):
        self.tape[self.ptr] -= 1

    def get(self):
        return self.tape[self.ptr]

    def set(self, val):
        self.tape[self.ptr] = val


def parse(source_code, bracket_matcher):
    cleaned_source_code = ""
    l_bracket_stack = []
    for char in source_code:
        if char in VALID_OPERATOR:
            if char == "[":
                l_bracket_stack.append(len(cleaned_source_code))
            elif char == "]":
                if len(l_bracket_stack) <= 0:
                    raise SyntaxError("Unmatched bracket.")
                l_bracket_pos = l_bracket_stack.pop()
                bracket_matcher[len(cleaned_source_code)] = l_bracket_pos
                bracket_matcher[l_bracket_pos] = len(cleaned_source_code)
            cleaned_source_code += char
    return cleaned_source_code


def jitpolicy(driver):
    from rpython.jit.codewriter.policy import JitPolicy
    return JitPolicy()


@purefunction
def get_matching_bracket(bracket_map, pc):
    return bracket_map[pc]


def execute(source_stream):
    bracket_match = {}
    source_code = parse(source_stream.readall(), bracket_match)
    pc = 0
    tape = Tape()
    while pc < len(source_code):
        jitdriver.jit_merge_point(pc=pc, tape=tape, source_code=source_code, bracket_match=bracket_match)
        operator = source_code[pc]
        if operator == ">":
            tape.move_right()
        elif operator == "<":
            tape.move_left()
        elif operator == "+":
            tape.inc()
        elif operator == "-":
            tape.dec()
        elif operator == "[":
            if tape.get() == 0:
                pc = get_matching_bracket(bracket_match, pc)
        elif operator == "]":
            pc = get_matching_bracket(bracket_match, pc) - 1  # Go back to l_bracket, -1 because we will increment pc by 1 later
        elif operator == ".":
            os.write(STDOUT_FD, chr(tape.get()))
        elif operator == ",":
            tape.set(ord(os.read(STDIN_FD, 1)[0]))
        else:
            raise RuntimeError("Unexpected operator. This should not happen.")
        pc += 1


def entry_point(argv):
    if len(argv) < 2:
        os.write(STDERR_FD, "Usage: bf <bf_source_file>\n")
        return 1
    file_path = argv[1]
    f = streamio.open_file_as_stream(file_path)
    execute(f)
    f.close()
    return 0


def target(*args):
    return entry_point


if "__main__" == __name__:
    entry_point(sys.argv)
