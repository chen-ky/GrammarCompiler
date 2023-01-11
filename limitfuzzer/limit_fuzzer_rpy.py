import os
from utils.random import random
from utils import StrSet, TupleSorter


class Fuzzer(object):
    def __init__(self, grammar):
        self.grammar = grammar
        self.system_name = os.uname()[0]  # expect "Darwin" and "Linux"

    def fuzz(self, key='<start>', max_num=None, max_depth=None):
        raise NotImplementedError()


class LimitFuzzer(Fuzzer):
    def __init__(self, grammar):
        # super(LimitFuzzer, self).__init__(grammar)
        self.grammar = grammar
        self.system_name = os.uname()[0]  # expect "Darwin" and "Linux"

        self.key_cost = {}
        self.cost = self.compute_cost(grammar)

    def symbol_cost(self, grammar, symbol, seen):
        if symbol in self.key_cost:
            return self.key_cost[symbol]
        if symbol in seen.get():
            self.key_cost[symbol] = float('inf')
            return float('inf')
        expansion_costs = []
        for rule in grammar.get(symbol, []):
            expansion_costs.append(self.expansion_cost(grammar, rule, seen.union(StrSet(symbol))))
        if len(expansion_costs) == 0:
            v = 0
        else:
            v = min(expansion_costs)
        self.key_cost[symbol] = v
        return v

    def expansion_cost(self, grammar, tokens, seen):
        symbol_costs = [0]
        for token in tokens:
            if token in grammar:
                symbol_costs.append(self.symbol_cost(grammar, token, seen))
        return max(symbol_costs) + 1

    def gen_key(self, key, depth, max_depth):
        if key not in self.grammar:
            return key
        if depth > max_depth:
            clst = []
            for rule in self.grammar[key]:
                clst.append((self.cost[key][str(rule)], rule))
            TupleSorter(clst).sort()
            rules = []
            for c, r in clst:
                if c == clst[0][0]:
                    rules.append(r)
        else:
            rules = self.grammar[key]
        result = self.gen_rule(random.choice(rules), depth+1, max_depth)
        return result

    def gen_rule(self, rule, depth, max_depth):
        result = ''
        for token in rule:
            result += self.gen_key(token, depth, max_depth)
        return result

    def fuzz(self, key='<start>', max_depth=10):
        return self.gen_key(key=key, depth=0, max_depth=max_depth)

    def compute_cost(self, grammar):
        cost = {}
        for k in grammar:
            cost[k] = {}
            for rule in grammar[k]:
                cost[k][str(rule)] = self.expansion_cost(grammar, rule, StrSet())
        return cost


# A non recursive version.
class LimitFuzzer_NR(LimitFuzzer):

    def __init__(self, grammar):
        # super(LimitFuzzer_NR, self).__init__(grammar)
        self.grammar = grammar
        self.system_name = os.uname()[0]  # expect "Darwin" and "Linux"

        self.key_cost = {}
        self.cost = self.compute_cost(grammar)

    def is_nt(self, name):
        return (name[0], name[-1]) == ('<', '>')

    def tree_to_str(self, tree):
        name, children = tree
        if not self.is_nt(name):
            return name
        tree_str = ""
        for c in children:
            tree_str += self.tree_to_str(c)
        return tree_str

    def nonterminals(self, rule):
        non_terminals = []
        for t in rule:
            if self.is_nt(t):
                non_terminals.append(t)
        return non_terminals

    def _get_def(self, t):
        if self.is_nt(t):
            return [t, None]
        else:
            return [t, []]

    def gen_key(self, key, max_depth):
        cheap_grammar = {}
        for k in self.cost:
            # should we minimize it here? We simply avoid infinities
            rules = self.grammar[k]
            costs = []
            for r in rules:
                costs.append(self.cost[k][str(r)])
            min_cost = min(costs)
            # grammar[k] = [r for r in grammar[k] if self.cost[k][str(r)] == float('inf')]
            grammars = []
            for r in self.grammar[k]:
                if self.cost[k][str(r)] == min_cost:
                    grammars.append(r)
            cheap_grammar[k] = grammars

        root = [key, None]
        queue = [(0, root)]
        while queue:
            # get one item to expand from the queue
            (depth, item) = queue.pop(0)
            key = item[0]
            if item[1] is not None:
                continue
            grammar = cheap_grammar
            if depth < max_depth:
                grammar = self.grammar
            chosen_rule = random.choice(grammar[key])
            expansion = []
            for t in chosen_rule:
                expansion.append(self._get_def(t))
            item[1] = expansion
            for t in expansion:
                queue.append((depth+1, t))
            # print("Fuzz: %s" % key, len(queue), file=sys.stderr)
        # print(file=sys.stderr)
        return root

    def fuzz(self, key='<start>', max_depth=10):
        return self.tree_to_str(self.gen_key(key=key, max_depth=max_depth))
