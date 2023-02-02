# Math equations
# grammar = {
#     "<start>": [["<expr>", "<newline>"]],
#     "<expr>": [["<expr>", "+", "<expr>"],
#                ["<expr>", "-", "<expr>"],
#                ["<expr>", "*", "<expr>"],
#                ["<expr>", "/", "<expr>"],
#                ["(", "<expr>", ")"],
#                ["<factor>"]],
#     "<factor>": [["<integer>"],
#                  ["<integer>", ".", "<integer>"],
#                  ["-", "<factor>"]],
#     "<integer>": [["<digit>", "<integer>"],
#                   ["<digit>"]],
#     "<digit>": [["0"], ["1"], ["2"], ["3"], ["4"],
#                 ["5"], ["6"], ["7"], ["8"], ["9"]],
#     "<newline>": [["\n"]]
# }

import string
# JSON
# Generate <character> rule
json_character_rule = []
json_character_exclude = [
    "\"",  # " char
    "\\"  # \ char
]

# UTF-8 uses variable length encoding
# https://www.unicode.org/versions/Unicode15.0.0/ch02.pdf#G11165
# See "ASCII Transparency" description for number of bytes character
# range are encoded with
# Also, http://www.adamponting.com/utf-8-1-and-2-byte-codes/ for the unicode to hex range
for c in string.ascii_letters:
    if c not in json_character_exclude:
        # b_array = bytearray(1)
        # b_array[0] = c
        json_character_rule.append([c])

# for c in range(0xc000, 0xdfff + 1):
#     b_array = bytearray(2)
#     if c not in json_character_exclude:
#         i = 0
#         while i < len(b_array):
#             b_array[-(i + 1)] = c % 256  # Populate byte from behind
#             c = c // 256
#             i += 1
#         json_character_rule.append([b_array])

# for c in range(0xe00000, 0xefffff + 1):
#     b_array = bytearray(3)
#     if c not in json_character_exclude:
#         i = 0
#         while i < len(b_array):
#             b_array[-(i + 1)] = c % 256  # Populate byte from behind
#             c = c // 256
#             i += 1
#         json_character_rule.append([b_array])

# for c in range(0xf0000000, 0xffffffff + 1):
#     b_array = bytearray(4)
#     if c not in json_character_exclude:
#         i = 0
#         while i < len(b_array):
#             b_array[-(i + 1)] = c % 256  # Populate byte from behind
#             c = c // 256
#             i += 1
#         json_character_rule.append([b_array])

json_character_rule.append(["\\", "<escape>"])

grammar = {
    "<start>": [["<element>"]],
    "<value>": [["<object>"], ["<array>"], ["<string>"], ["<number>"], ["true"], ["false"], ["null"]],
    "<object>": [["{", "<ws>", "}"], ["{", "<members>", "}"]],
    "<members>": [["<member>"], ["<member>", ",", "<members>"]],
    "<member>": [["<ws>", "<string>", "<ws>", ":", "<element>"]],
    "<array>": [["[", "<ws>", "]"], ["[", "<elements>", "]"]],
    "<elements>": [["<element>"], ["<element>", ",", "<elements>"]],
    "<element>": [["<ws>", "<value>", "<ws>"]],
    "<string>": [["\"", "<characters>", "\""]],
    "<characters>": [["<empty>"], ["<character>", "<characters>"]],
    "<character>": json_character_rule,
    "<escape>": [["\""], ["\\"], ["/"], ["b"], ["f"], ["n"], ["r"], ["t"], ["u", "<hex>", "<hex>", "<hex>", "<hex>"]],
    "<hex>": [["<digit>"], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["A"], ["B"], ["C"], ["D"], ["E"], ["F"]],
    "<number>": [["<integer>", "<fraction>", "<exponent>"]],
    "<integer>": [["<digit>"], ["<onenine>", "<digits>"], ["-", "<digit>"], ["-", "<onenine>", "<digits>"]],
    "<digits>": [["<digit>"], ["<digit>", "<digits>"]],
    "<digit>": [["0"], ["<onenine>"]],
    "<onenine>": [["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]],
    "<fraction>": [["<empty>"], [".", "<digits>"]],
    "<exponent>": [["<empty>"], ["E", "<sign>", "<digits>"], ["e", "<sign>", "<digits>"]],
    "<sign>": [["<empty>"], ["+"], ["-"]],
    "<ws>": [["<empty>"], [" ", "<ws>"], ["\n", "<ws>"], ["\r", "<ws>"], ["\t", "<ws>"]],
    "<empty>": [[]]
}
