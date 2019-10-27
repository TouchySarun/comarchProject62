from my_utils import (
    to_binary_str,
    binary_str_to_decimal,
    check_offset_field,
    check_isregister,
)


def lw(field0, field1, field2):
    opcode = "010"
    code = remain_code(opcode, field0, field1, field2)
    return binary_str_to_decimal(code)


def sw(field0, field1, field2):
    opcode = "011"
    code = remain_code(opcode, field0, field1, field2)
    return binary_str_to_decimal(code)


def beq(field0, field1, field2):
    opcode = "100"
    code = remain_code(opcode, field0, field1, field2)
    return binary_str_to_decimal(code)


def remain_code(opcode, field0, field1, field2):

    if (
        check_isregister(field0)
        and check_isregister(field1)
        and check_offset_field(field2)
    ):
        code = ""
        binaryField0 = to_binary_str(field0, 3)
        binaryField1 = to_binary_str(field1, 3)

        code += binaryField0
        code += binaryField1

        binaryField2 = to_binary_str(field2, 16)
        code += binaryField2

        return opcode + code


# print(lw(0, 1, 7))
# print(lw(1, 2, 3))
# print(beq(0, 1, 2))

