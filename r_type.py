from my_utils import binary_str_to_decimal, check_offset_field, to_binary_str

# R-Type
# 31-25,15-3 don't care , 24-22 opcode , 21-19 rs , 18-16 rt , 2-0 rd
def add(rd, rs, rt):
    if check_offset_field(rs) and check_offset_field(rt):
        rd = rs + rt
        instruction = '0000000000' + to_binary_str(rs, 3) + to_binary_str(rt, 3) + '000000000000' + to_binary_str(rd, 3)
        # return instruction
        return binary_str_to_decimal(instruction)

def nand(rd, rs, rt):
    if check_offset_field(rs) and check_offset_field(rt) :
        rd = not (rs & rt)
        instruction = '0000000001' + to_binary_str(rs, 3) + to_binary_str(rt, 3) + '000000000000' + to_binary_str(rd, 3)
        # return instruction
        return binary_str_to_decimal(instruction)

# Test function  
# x = 0
# y = 0
# print(add(x, 1, 2))
# print(nand(y, 0, 1))