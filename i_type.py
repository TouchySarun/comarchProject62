from my_utils import (
    to_binary_str,
    binary_str_to_decimal,
    check_offset_field,
    check_isregister,
)

# # add binary
# def addBinary(x, y):
#     max_len = max(len(x), len(y))

#     x = x.zfill(max_len)
#     y = y.zfill(max_len)
#     result = ""
#     carry = 0

#     for i in range(max_len - 1, -1, -1):
#         c = carry
#         if x[i] == "1":
#             c += 1
#         else:
#             c += 0

#         if y[i] == "1":
#             c += 1
#         else:
#             c += 0

#         if c % 2 == 1:
#             result = "1" + result
#         else:
#             result = "0" + result

#         if c < 2:
#             carry = 0
#         else:
#             carry = 1

#     if carry != 0:
#         result = "1" + result

#     return result.zfill(max_len)


# # two complement
# def twoCom(num):
#     leng = len(num)
#     oneCom = ""
#     count = 0
#     while count < leng:
#         if int(num[count]) == 0:
#             oneCom += "1"
#         elif int(num[count]) == 1:
#             oneCom += "0"
#         count += 1
#     return addBinary(oneCom, "1")


# # main
# inputCommand = input("command: ")
# data = inputCommand.split()

# label = str(data[0])
# instruction = str(data[1])
# field0 = int(data[2])  # regA
# field1 = int(data[3])  # regB
# field2 = int(data[4])  # offsetField
# comments = str(data[5])


# if not check_isregister(field0) or not check_isregister(field1):
#     pass
# elif not check_offset_field(field2):
#     pass
# else:
#     code = "0000000"

#     if instruction == "lw":
#         code += "010"
#     elif instruction == "sw":
#         code += "011"
#     elif instruction == "beq":
#         code += "100"

#     binaryField0 = to_binary_str(field0, 3)
#     binaryField1 = to_binary_str(field1, 3)

#     code += binaryField0
#     code += binaryField1

#     binaryField2 = to_binary_str(field2, 16)
#     code += twoCom(binaryField2)

#     print("machine code is: ", code)
#     print("value is: ", int(code, 2))


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


# print(lw(0, 1, 7))
# print(lw(1, 2, 3))
# print(beq(0, 1, 2))

