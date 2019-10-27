from my_utils import to_binary_str, binary_str_to_decimal, check_offset_field, check_isregister

def jalr(x0, x1):
    ans = "101"
    if check_isregister(x0) :
        bi0 = to_binary_str(x0, 3)
        ans = ans + bi0
    
    if check_offset_field(x1) :
        bi1 = to_binary_str(x1, 3)
        ans = ans + bi1
        ans = ans + '0000000000000000'

    return binary_str_to_decimal(ans)


a = input()
ar = a.split(' ')
print(jalr(int(ar[0]), int(ar[1])))

