from my_utils import extract_binary


def jalr(code, g):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 18, 16)

    g["reg"][regB] = g["PC"] + 1
    g["PC"] = g["reg"][regA]

