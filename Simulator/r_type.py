from my_utils import to_binary_str, binary_str_to_decimal, check_offset_field

# R-Type
def nand(code, global):
    field1 = binary_str_to_decimal(code[2:0])
    field2 = binary_str_to_decimal(code[21:19])
    field3 = binary_str_to_decimal(code[18:16])
    global['mem'][] = not ( global['mem'][rs] &  global['mem'][rt] )  
    ic += 1
    pc += 4

