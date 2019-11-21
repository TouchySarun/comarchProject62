def halt(code, computer):
    computer.go_next_pc()
    computer.halt = True


def noop(code, computer):
    computer.go_next_pc()

