import sys
from grammar import grammar as g


RULE_FN_STARTS_WITH = "rule_"
RULE_TEMPLATE = "def {}%s():\n%s".format(RULE_FN_STARTS_WITH)


def generate_rule_fn(grammar, key):
    if key not in grammar:
        return None
    statements = grammar[key]
    statements_len = len(statements)
    sub_fn_string = "" if statements_len <= 1 else "    rand = random.randint(0, {})\n".format(statements_len - 1)
    for (i, statement) in enumerate(statements):
        if statements_len > 1:
            sub_fn_string += "    if rand == {}:\n".format(i)
        for item in statement:
            if item in grammar:
                sub_fn_string += "{}{}{}()\n".format(' ' * 8 if statements_len > 1 else ' ' * 4, RULE_FN_STARTS_WITH, item.strip('<>'))
            else:
                sub_fn_string += "{}print(\"{}\", end=\"\")\n".format(' ' * 8 if statements_len > 1 else ' ' * 4, item)
    fn_string = RULE_TEMPLATE % (key.strip("<>"), sub_fn_string)
    return fn_string


def entry_point(argv):
    print "import random\n"
    for key in g.keys():
        print generate_rule_fn(g, key)
    print "\nrule_start()"

def target(*args):
    return entry_point

if "__main__" == __name__:
    entry_point(sys.argv)
    
