from r_type import add, nand
from i_type import lw, sw, beq
from j_type import jalr
from o_type import halt, noop

instructions_opcode = {
    0: {"function": add},
    1: {"function": nand},
    2: {"function": lw},
    3: {"function": sw},
    4: {"function": beq},
    5: {"function": jalr},
    6: {"function": halt},
    7: {"function": noop},
}
