# Elimination-of-ambiguity.py

def remove_left_recursion(grammar):
    new_grammar = {}

    for non_terminal in grammar:
        alpha = []
        beta = []

        for production in grammar[non_terminal]:
            if production[0] == non_terminal:
                alpha.append(production[1:])
            else:
                beta.append(production)

        if alpha:
            new_nt = non_terminal + "'"
            new_grammar[non_terminal] = [b + [new_nt] for b in beta]
            new_grammar[new_nt] = [a + [new_nt] for a in alpha] + [['ε']]
        else:
            new_grammar[non_terminal] = grammar[non_terminal]

    return new_grammar


def left_factoring(grammar):
    new_grammar = {}

    for head in grammar:
        prefixes = {}
        for prod in grammar[head]:
            prefix = prod[0]
            prefixes.setdefault(prefix, []).append(prod)

        if any(len(v) > 1 for v in prefixes.values()):
            new_nt = head + "_factored"
            new_grammar[head] = []
            new_grammar[new_nt] = []

            for prefix, prods in prefixes.items():
                if len(prods) > 1:
                    new_grammar[head].append([prefix, new_nt])
                    for p in prods:
                        new_grammar[new_nt].append(p[1:])
                else:
                    new_grammar[head].append(prods[0])
        else:
            new_grammar[head] = grammar[head]

    return new_grammar
