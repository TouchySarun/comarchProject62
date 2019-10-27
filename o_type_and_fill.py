from my_utils import binary_str_to_decimal

#O-type
def noop(noop):
    instruction = '111' + '0000000000000000000000'
    return binary_str_to_decimal(instruction)
print(noop(noop))

def halt(halt):
    instruction = '110' + '0000000000000000000000'
    return binary_str_to_decimal(instruction)
print(halt(halt))

#.fill
# def fill(input):


# getinput = input()
# fill(getinput)