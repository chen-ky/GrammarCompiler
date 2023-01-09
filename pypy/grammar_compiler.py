from grammar import grammar as g
from typing import Union


RULE_FN_STARTS_WITH = "rule_"
RULE_TEMPLATE = f"""
def {RULE_FN_STARTS_WITH}%s():
%s
"""


def generate_rule_fn(grammar: dict[str, tuple[list[str]]],
                     key: str) -> Union[str, None]:
    if key not in grammar:
        return None
    statements = grammar[key]
    statements_len = len(statements)
    sub_fn_string = "" if statements_len <= 1 else f"    rand = random.randint(0, {statements_len - 1})\n"
    for (i, statement) in enumerate(statements):
        if statements_len > 1:
            sub_fn_string += f"    if rand == {i}:\n"
        for item in statement:
            if item in grammar:
                sub_fn_string += f"{' ' * 8 if statements_len > 1 else ' ' * 4}{RULE_FN_STARTS_WITH}{item.strip('<>')}()\n"
            else:
                sub_fn_string += f"{' ' * 8 if statements_len > 1 else ' ' * 4}print(\"{item}\", end=\"\")\n"
    fn_string = RULE_TEMPLATE % (key.strip("<>"), sub_fn_string)
    return fn_string


if "__main__" == __name__:
    # print(g)
    print("import random\n")
    for key in g.keys():
        print(generate_rule_fn(g, key), end="")
    print("\nrule_start()")
