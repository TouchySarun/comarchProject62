from my_utils import extract_binary, clamp_value
from all_instruction import instructions_opcode
from register_value import RegisterValue


class ComputerValue:
    def __init__(self):
        self._reg = [0, 0, 0, 0, 0, 0, 0, 0]
        self._mem = {}
        self.pc = 0
        self.ic = 0
        self.halt = False

    # Access register
    def set_register(self, index, value):
        if index < 0 or index > 7:
            raise Exception(f"Can't Access register {index}")
        if index != 0:
            self._reg[index] = clamp_value(value)


    def get_register(self, index):
        if index < 0 or index > 7:
            raise Exception(f"Can't Access register {index}")
        return self._reg[index]

    # Accress memory
    def set_memory(self, index, value):
        if index < 0:
            raise Exception(f"Can't Access memory {index}")
        self._mem[index] = clamp_value(value)

    def get_memory(self, index):
        if index < 0:
            raise Exception(f"Can't Access memory {index}")
        return self._mem.get(index, 0)

    def print_state(self):
        print("@@@")
        print("state")
        print(f"\t pc = {self.pc}")
        print(f"\t memory:")
        for i, mem in self._mem.items():
            print(f"\t\tmem[{i}]:{mem}")
        print(f"\t regiters:")
        for i, reg in enumerate(self._reg):
            print(f"\t\treg[{i}]:{reg}")
        print("end state\n")


if __name__ == "__main__":
    machine_code_file = input("Machine code file: ")

    computer = ComputerValue()

    with open(machine_code_file, "r") as file_reader:
        # read input machine code
        for line_count, line in enumerate(file_reader):
            computer.set_memory(line_count, int(line))

    computer.print_state()

    while not computer.halt:
        try:
            pc = computer.pc
            code = computer.get_memory(pc)
            opcode = extract_binary(code, 22, 24)

            # call function according to opcode
            instruction_handler = instructions_opcode[opcode]["function"]
            instruction_handler(code, computer)

            computer.ic += 1

        except Exception as e:
            print(f"Error {e}")
            exit(1)


        if computer.halt:
            print("machine halted")
            print(f"total of {computer.ic} instructions executed")
            print("final state of machine:")

        computer.print_state()
        # input("Press Enter to continue...")

