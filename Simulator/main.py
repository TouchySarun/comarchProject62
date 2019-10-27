from my_utils import to_binary_str
from all_instruction import instructions

GLOBAL_VALUE = {
    "pc": 0,
    "ic": 0,
    "reg": [0,0,0,0,0,0,0,0],
    "mem": []
}

if __name__ == "__main__":
    machine_code_file = input("Machine code file: ")

    with open(machine_code_file, "r") as file_reader:
        for content in file_reader:
            GLOBAL_VALUE["mem"].append(int(content))
    
    
    while GLOBAL_VALUE["pc"] < len(GLOBAL_VALUE["mem"]):
    # look at pc
        pc = GLOBAL_VALUE["pc"]
        code = GLOBAL_VALUE["mem"][pc]

        
        code_binary = to_binary_str(code, 32)
        opcode = code_binary[32-25:32-22]

        arg = code_binary[32-22:]

        instructions[opcode]["function"](arg, GLOBAL_VALUE)
        

        GLOBAL_VALUE["pc"] += 1




    print(GLOBAL_VALUE)