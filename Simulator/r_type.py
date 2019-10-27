from my_utils import binary_str_to_decimal, extract_binary

def add (code,g):
    regA = extract_binary(code,19,21)
    regB = extract_binary(code,16,18)
    destReg = extract_binary(code,0,2)

    g["reg"][destReg] = g["reg"][regA] + g["reg"][regB]
    g["pc"] += 1