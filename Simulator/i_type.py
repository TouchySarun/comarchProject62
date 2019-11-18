from my_utils import extract_binary


def lw(code, computer):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    offsetField = extract_binary(code, 0, 15, unsiged=False)

    address = computer.get_register(regA) + offsetField
    mem_value = computer.get_memory(address)
    computer.set_register(regB, mem_value)
    computer.pc += 1


def sw(code, computer):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    offsetField = extract_binary(code, 0, 15, unsiged=False)

    address = computer.get_register(regA) + offsetField
    regB_value = computer.get_register(regB)
    computer.set_memory(address, regB_value)
    computer.pc += 1


def beq(code, computer):
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    offsetField = extract_binary(code, 0, 15, unsiged=False)

    regA_value = computer.get_register(regA)
    regB_value = computer.get_register(regB)

    if regA_value == regB_value:
        computer.pc += 1 + offsetField
    else:
        computer.pc += 1

