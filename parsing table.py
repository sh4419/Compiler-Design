# parsing-table.py

def build_parsing_table(grammar, FIRST, FOLLOW):
    table = {}

    for head in grammar:
        table[head] = {}

        for production in grammar[head]:
            first_set = set()

            for symbol in production:
                first_set |= (FIRST[symbol] - {'ε'})
                if 'ε' not in FIRST[symbol]:
                    break
            else:
                first_set.add('ε')

            for terminal in first_set:
                if terminal != 'ε':
                    table[head][terminal] = production

            if 'ε' in first_set:
                for terminal in FOLLOW[head]:
                    table[head][terminal] = production

    return table
