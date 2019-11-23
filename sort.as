    add 0 0 2
L1 add 0 0 3
L2 lw 0 1 four
    beq 3 1 addi
    lw 0 1 arr
    add 1 3 1
    lw 1 4 0
    lw 0 6 one
    add 1 6 1
    lw 1 6 0
    nand 6 6 6
    lw 0 7 one
    add 6 7 6
    add 4 6 7
    lw 0 1 sign
    nand 1 7 7
    nand 7 7 7
    lw 0 5 one
    add 3 5 3
    beq 1 7 swap
    beq 0 0 L2
swap lw 0 1 arr
    add 1 3 1
    lw 1 4 -1
    lw 1 6 0
    sw 1 6 -1
    sw 1 4 0
    beq 0 0 L2
addi lw 0 1 one
    add 2 1 2
    lw 0 1 five
    beq 2 1 return
    beq 0 0 L1
return halt
one .fill 1
four .fill 4
five .fill 5
sign .fill 2147483648
arr .fill 39
    .fill 1
    .fill 2
    .fill 5
    .fill 8
    .fill 9