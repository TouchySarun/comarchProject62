from my_utils import extract_binary


def nand(code, computer):
    destReg = extract_binary(code, 0, 2)
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)

    value = ~(computer.get_register(regA) & computer.get_register(regB))
    computer.set_register(destReg, value)
    computer.pc += 1


def add(code, computer):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    destReg = extract_binary(code, 0, 2)

    value = computer.get_register(regA) + computer.get_register(regB)
    computer.set_register(destReg, value)
    computer.pc += 1

