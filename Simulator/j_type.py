from my_utils import  binary_str_to_decimal,extract_binary
 
def jal(code,global):
    field0 = extract_binary(code,19,21)
    field1 = extract_binary(code,18,16)

    global["reg"][field1] = global["PC"]+1
    global["PC"] = global["reg"][field0]



