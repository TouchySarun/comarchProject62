    lw  0   1   n
    lw  0   2   r
    lw  0   3   0
    lw  0   4   one
    lw  0   5   stack
    lw  0   6   subAdr
    jalr    6   7
    halt
comb    beq 1   2   out1
        beq 0   2   out1      
        beq 2   4   outn
        sw  0   7   stack   //sp(0) = x7 address
        add 4   5   5   //sp += 1
        sw  5   1   stack   //sp(1) = x1 input n
        add 4   5   5   
        sw  5   2   stack   //sp(2) = x2 input r
        add 4   5   5
        sw  5   3   stack   //sp(3) = x3 output
        lw  0   6   neg1    //x6 = -1
        add 1   6   1   //x1 = x1 + x6
        lw  0   6   subAdr  //x6 = addr(comb)
        jalr    6   7   //jal x7,comb
        lw  5   6   stack
        add 3   6   3
        lw  0   6   neg1
        add 2   6   2   //x2 = x2 + x6
        jalr    6   7   //jal x7,comb
        lw  5   6   stack
        sw  5   6   stack   //sw x6,3(sp)   
        
        lw  5   6   stack   //lw x6,3(sp)
        add 0   3   6   //x6 = x6 + x3

        lw  0   6   neg1    //x6 = -1
        add 2   6   2   //add x2,x2,x6
        lw  0   6   subAdr //x6 = addr(comb)
        jalr    6   7   //jal x1,comb
        lw  0   6   stack   //lw x6,0(sp)
        add 3   6   3       //add x12 = x12 1+ x6
        
        sw  0   3   stack   //sw x12,0(sp)
        lw  0   1   


out1    lw  0   3   one
        jalr    7   6
outn    lw  0   3   1
        jalr    7   6
pos1    .fill   1
neg1    .fill   -1
n   .fill   2
r   .fill   1
subAdr  .fill   comb
stack   .fill   0