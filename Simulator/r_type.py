from my_utils import extract_binary

# R-Type
def nand(code, global):
    destReg = extract_binary(code, 0, 2)
    regA = extract_binary(code, 19, 21)
    regB = extract_binary(code, 16, 18)
    
    global['mem'][destReg] = ~(global['mem'][regA] & global['mem'][regB])  
    global['pc'] += 1