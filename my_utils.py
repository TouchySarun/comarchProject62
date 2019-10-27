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

