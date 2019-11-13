from r_type import add, nand
from i_type import lw, sw, beq
from j_type import jalr
from o_type import halt, noop

instructions_opcode = {
    0: {"function": add, "name": "add"},
    1: {"function": nand, "name": "nand"},
    2: {"function": lw, "name": "lw"},
    3: {"function": sw, "name": "sw"},
    4: {"function": beq, "name": "beq"},
    5: {"function": jalr, "name": "jalr"},
    6: {"function": halt, "name": "halt"},
    7: {"function": noop, "name": "noop"},
}
