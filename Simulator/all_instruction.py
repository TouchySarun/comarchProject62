from r_type import add, nand
from i_type import lw, sw, beq
from j_type import jalr
from o_type import halt, noop

instructions = {
    "000":{
        "name": "add",
        "function": add
    },
    "001":{
        "name": "nand",
        "function": nand
    },
    "010":{
        "name": "lw",
        "function": lw
    },
    "011":{
        "name": "sw",
        "function": sw
    },
    "100":{
        "name": "beq",
        "function": beq
    },
    "101":{
        "name": "jalr",
        "function": jalr
    },
    "110":{
        "name": "halt",
        "function": halt
    },
    "111":{
        "name": "noop",
        "function": noop
    },
}