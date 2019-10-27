def to_binary_str(number, mask):
    binary_str = ""
    while mask > 0:
        current_bit = number & 1
        binary_str = str(current_bit) + binary_str
        number >>= 1
        mask -= 1
    return binary_str


def binary_str_to_decimal(binary):
    decimal = 0
    i = len(binary) - 1
    for bit in binary:
        decimal += int(bit) * (2 ** i)
        i -= 1
    return decimal


def extract_binary(num ,start, end, unsiged=True):
    count_bit = (end-start)+1
    i = 2**(count_bit)-1
    i <<= start
    extracted_bit = (num & i) >> start
    if unsiged:
        return extracted_bit

    signed_bit = ((1 << (count_bit-1)) & extracted_bit ) >> (count_bit-1)
    if not signed_bit:
        return extracted_bit

    return extracted_bit - 2**(count_bit)
    

def check_offset_field(num):
    if num < -32768 or num > 32767:
        raise Exception(f"error {num} offset overflow")
    return True


def check_isregister(num):
    if num < 0 or num > 7:
        raise Exception(f"error {num} not register")
    return True