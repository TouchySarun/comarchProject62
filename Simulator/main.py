from my_utils import to_binary_str, extract_binary
from all_instruction import instructions

GLOBAL_VALUE = {
    "pc": 0,
    "ic": 0,
    "reg": [0,0,0,0,0,0,0,0],
    "mem": [],
    "halt": False
}

def print_state(g):
    print("@@@")
    print("state")
    print(f"\t pc = {g['pc']}")
    print(f"\t memory:")
    for i,mem in enumerate(g["mem"]):
        print(f"\t\tmem[{i}]:{mem}")
    print(f"\t regiters:")
    for i,reg in enumerate(g["reg"]):
        print(f"\t\treg[{i}]:{reg}")
    print("end state")
    

if __name__ == "__main__":
    machine_code_file = input("Machine code file: ")

    with open(machine_code_file, "r") as file_reader:
        for line_count, line in enumerate(file_reader):
            GLOBAL_VALUE["mem"].append(int(line))
            print(f"mem[{line_count}]={GLOBAL_VALUE['mem'][line_count]}")
    
    
    while not GLOBAL_VALUE["halt"]:
    # look at pc
        pc = GLOBAL_VALUE["pc"]
        code = GLOBAL_VALUE["mem"][pc]
        opcode = to_binary_str(extract_binary(code, 22, 24),3)
        instructions[opcode]["function"](code, GLOBAL_VALUE)
        GLOBAL_VALUE["ic"] += 1

        if GLOBAL_VALUE["halt"]:
                print(f"""machine halted
total of {GLOBAL_VALUE["ic"]} instructions executed
final state of machine:""")

        print_state(GLOBAL_VALUE)


