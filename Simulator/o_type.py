def halt(code, computer):
    computer.pc += 1
    computer.halt = True


def noop(code, computer):
    computer.pc += 1

