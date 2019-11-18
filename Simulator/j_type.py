from my_utils import extract_binary


def jalr(code, computer):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)

    next_instruction = computer.pc + 1
    computer.set_register(regB, next_instruction)
    computer.pc = computer.get_register(regA)

