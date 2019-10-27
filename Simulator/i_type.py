from my_utils import binary_str_to_decimal, extract_binary

def lw (code,g):
    regA = extract_binary(code,19,21)
    regB = extract_binary(code,16,18)
    offsetField = extract_binary(code,0,15)

    address = g["reg"][regA] + g["reg"][offsetField]
    g["reg"][regB] = g["mem"][address]
    g["pc"] += 1


def sw(code,g):
    regA = extract_binary(code,19,21)
    regB = extract_binary(code,16,18)
    offsetField = extract_binary(code,0,15)

    address = g["reg"][regA] + g["reg"][offsetField]
    g["mem"][address] = g["reg"][regB]
    g["pc"] += 1

def beq(code,g):
    regA = extract_binary(code,19,21)
    regB = extract_binary(code,16,18)
    offsetField = extract_binary(code,0,15)

    if g["reg"][regA] == g["reg"][regB]:
        g["pc"] += 1 + offsetField





