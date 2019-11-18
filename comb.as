    lw     0       1       n
    lw     0       2       r
    lw     0       5       stack
    lw     0       4       six
    jalr   4       7
    halt
start   lw      0       6       one
    add    6       5       5
    sw     5       7       0
    add    6       5       5
    sw     5       1       0
    add    6       5       5
    sw     5       2       0
    add    6       5       5
    lw     0       3       one
    beq    1       2       return
    beq    2       0       return
    add    0       1       3
    beq    2       6       return
    lw     0       6       mone
    add    1       6       1
    jalr   4       7
    sw     5       3       0
    lw     5       1       -2
    lw     5       2       -1
    lw     0       6       mone
    add    2       6       2
    add    1       6       1
    jalr   4       7
    lw     5       6       0
    add    3       6       3
return  lw      0       6       mfour
    lw     5       7       -3
    add    5       6       5
    jalr   7       0
six     .fill   6
mone    .fill   -1
mfour   .fill   -4
one     .fill   1
n       .fill   6
r       .fill   3
stack   .fill   41
