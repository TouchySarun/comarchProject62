from my_utils import extract_binary


def lw(code, g):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    offsetField = extract_binary(code, 0, 15, unsiged=False)

    address = g["reg"][regA] + offsetField
    g["reg"][regB] = g["mem"][address]
    g["pc"] += 1


def sw(code, g):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    offsetField = extract_binary(code, 0, 15, unsiged=False)

    address = g["reg"][regA] + offsetField
    g["mem"][address] = g["reg"][regB]
    g["pc"] += 1


def beq(code, g):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    offsetField = extract_binary(code, 0, 15, unsiged=False)

    if g["reg"][regA] == g["reg"][regB]:
        g["pc"] += 1 + offsetField
    else:
        g["pc"] += 1

