# lexical-analyzer.py

import re

TOKEN_SPECIFICATION = [
    ('NUMBER',   r'\d+(\.\d*)?'),
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
    ('ASSIGN',   r'='),
    ('END',      r';'),
    ('OP',       r'[+\-*/]'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
    ('MISMATCH', r'.'),
]

KEYWORDS = {'if', 'else', 'while', 'int', 'float', 'return'}

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPECIFICATION)

def lexer(code):
    tokens = []
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)

        elif kind == 'ID' and value in KEYWORDS:
            kind = value.upper()

        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue

        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')

        tokens.append((kind, value))

    return tokens


if __name__ == "__main__":
    code = "int a = 5 + 3;"
    print(lexer(code))
