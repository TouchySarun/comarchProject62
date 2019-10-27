from my_utils import binary_str_to_decimal, check_offset_field, to_binary_str

#O-type
def noop():
    return binary_str_to_decimal(f"111{to_binary_str(0,22)}")
print(noop())

def halt():
    return binary_str_to_decimal(f"110{to_binary_str(0,22)}")
print(halt())

#.fill
def fill(input):
    if check_offset_field(input):
        return input
