from my_utils import extract_binary


def jalr(code, g):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)

    g["reg"][regB] = g["pc"] + 1
    g["pc"] = g["reg"][regA]

