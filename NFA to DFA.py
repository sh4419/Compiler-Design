# NFA-to-DFA.py

def epsilon_closure(states):
    stack = list(states)
    closure = set(states)

    while stack:
        state = stack.pop()
        for next_state in state.epsilon:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)

    return closure


def move(states, symbol):
    result = set()
    for state in states:
        if symbol in state.edges:
            result.update(state.edges[symbol])
    return result


def nfa_to_dfa(nfa, symbols):
    start_state = frozenset(epsilon_closure([nfa.start]))
    dfa_states = {start_state: {}}
    unmarked = [start_state]

    while unmarked:
        current = unmarked.pop()

        for symbol in symbols:
            next_states = epsilon_closure(move(current, symbol))
            next_states = frozenset(next_states)

            if next_states not in dfa_states:
                dfa_states[next_states] = {}
                unmarked.append(next_states)

            dfa_states[current][symbol] = next_states

    return dfa_states
