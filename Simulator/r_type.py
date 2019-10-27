from my_utils import extract_binary


def nand(code, g):
    destReg = extract_binary(code, 0, 2)
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)

    g["mem"][destReg] = ~(g["mem"][regA] & g["mem"][regB])
    g["pc"] += 1


def add(code, g):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    destReg = extract_binary(code, 0, 2)

    g["reg"][destReg] = g["reg"][regA] + g["reg"][regB]
    g["pc"] += 1

