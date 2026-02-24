# Regular-expression-to-NFA.py

class State:
    def __init__(self):
        self.edges = {}
        self.epsilon = []

class NFA:
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept


def regex_to_nfa(regex):
    stack = []

    for char in regex:
        if char == '*':
            nfa = stack.pop()
            start = State()
            accept = State()
            start.epsilon += [nfa.start, accept]
            nfa.accept.epsilon += [nfa.start, accept]
            stack.append(NFA(start, accept))

        elif char == '.':  # concatenation
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.accept.epsilon.append(nfa2.start)
            stack.append(NFA(nfa1.start, nfa2.accept))

        elif char == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start = State()
            accept = State()
            start.epsilon += [nfa1.start, nfa2.start]
            nfa1.accept.epsilon.append(accept)
            nfa2.accept.epsilon.append(accept)
            stack.append(NFA(start, accept))

        else:
            start = State()
            accept = State()
            start.edges[char] = [accept]
            stack.append(NFA(start, accept))

    return stack.pop()
