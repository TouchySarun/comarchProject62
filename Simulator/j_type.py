from my_utils import  binary_str_to_decimal,extract_binary
 
def jalr(code, g):
    field0 = extract_binary(code,19,21)
    field1 = extract_binary(code,18,16)

    g["reg"][field1] = g["PC"]+1
    g["PC"] = g["reg"][field0]



