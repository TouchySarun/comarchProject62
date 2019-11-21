from my_utils import extract_binary, clamp_value
from all_instruction import instructions_opcode


class ComputerValue:
    def __init__(self):
        self._reg = [0, 0, 0, 0, 0, 0, 0, 0]
        self._mem = {}
        self._pc = 0
        self.ic = 0
        self.halt = False
        self.numMemory = 0

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

    def read_instruction_input(self, file_input):
        instruction_mem = 0
        with open(file_input, "r") as file_reader:
            # read input machine code
            for line_count, line in enumerate(file_reader):
                self.set_memory(line_count, int(line))
                instruction_mem += 1
        
        computer.numMemory = instruction_mem
    
    # pc managing
    def set_pc(self, new_pc):
        if new_pc >= self.numMemory:
            raise Exception(f"PC can't go to {new_pc}")
        self._pc = new_pc
    
    def get_pc(self):
        return self._pc
    
    def go_next_pc(self):
        self.set_pc(self._pc + 1)

    def print_state(self):
        print("\n@@@")
        print("state:")
        print(f"\tpc {self._pc}")
        print(f"\tmemory:")
        for i, mem in self._mem.items():
            print(f"\t\tmem[ {i} ] {mem}")
        print(f"\tregiters:")
        for i, reg in enumerate(self._reg):
            print(f"\t\treg[ {i} ] {reg}")
        print("end state")

        # printf("\n@@@\nstate:\n");
        # printf("\tpc %d\n", statePtr->pc);
        # printf("\tmemory:\n");
        # for (i=0; i<statePtr->numMemory; i++) {
        #     printf("\t\tmem[ %d ] %d\n", i, statePtr->mem[i]);
        # }
        # printf("\tregisters:\n");
        # for (i=0; i<NUMREGS; i++) {
        #     printf("\t\treg[ %d ] %d\n", i, statePtr->reg[i]);
        # }
        # printf("end state\n");


if __name__ == "__main__":
    machine_code_file = input("Machine code file: ")

    computer = ComputerValue()

    computer.read_instruction_input(machine_code_file)

    computer.print_state()

    while not computer.halt:
        try:
            pc = computer.get_pc()
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

