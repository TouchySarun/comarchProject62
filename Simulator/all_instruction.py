def fool(*arg):
    print(arg)

instructions = {
    "000":{
        "name": "add",
        "function": fool
    },
    "001":{
        "name": "nand",
        "function": fool
    },
    "010":{
        "name": "lw",
        "function": fool
    },
    "011":{
        "name": "sw",
        "function": fool
    },
    "100":{
        "name": "beq",
        "function": fool
    },
    "101":{
        "name": "jalr",
        "function": fool
    },
    "110":{
        "name": "halt",
        "function": fool
    },
    "111":{
        "name": "noop",
        "function": fool
    },
}