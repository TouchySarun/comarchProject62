from j_type import jalr
from o_type_fill import halt, noop, fill
from i_type import lw, beq, sw
from r_type import add, nand


def fool(temp=0, temp1=1, temp2=2):
    print(temp)
    print(temp1)
    print(temp2)


instructions = {
    "add": {"input": 3, "function": add},
    "nand": {"input": 3, "function": nand},
    "lw": {"input": 3, "function": lw},
    "sw": {"input": 3, "function": sw},
    "beq": {"input": 3, "function": beq},
    "jalr": {"input": 2, "function": jalr},
    "halt": {"input": 0, "function": halt},
    "noop": {"input": 0, "function": noop},
    ".fill": {"input": 1, "function": fill},
}
