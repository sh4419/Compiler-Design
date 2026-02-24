# first-and-follow.py

from collections import defaultdict

def compute_first(grammar):
    FIRST = defaultdict(set)

    def first(symbol):
        if symbol not in grammar:
            return {symbol}

        for production in grammar[symbol]:
            if production == ['ε']:
                FIRST[symbol].add('ε')
            else:
                for sym in production:
                    sym_first = first(sym)
                    FIRST[symbol] |= (sym_first - {'ε'})
                    if 'ε' not in sym_first:
                        break
                else:
                    FIRST[symbol].add('ε')

        return FIRST[symbol]

    for non_terminal in grammar:
        first(non_terminal)

    return FIRST


def compute_follow(grammar, FIRST, start_symbol):
    FOLLOW = defaultdict(set)
    FOLLOW[start_symbol].add('$')

    for _ in range(5):
        for head, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        rest = production[i+1:]
                        if rest:
                            first_rest = set()
                            for sym in rest:
                                first_rest |= (FIRST[sym] - {'ε'})
                                if 'ε' not in FIRST[sym]:
                                    break
                            FOLLOW[symbol] |= first_rest
                        else:
                            FOLLOW[symbol] |= FOLLOW[head]

    return FOLLOW
