    lw 0 1 mcand
    lw 0 2 mplier
    lw 0 4 one
    lw 0 7 count
loop nand 2 4 6
    nand 6 6 6
    beq 4 7 exit
    beq 4 6 plus
next add 1 1 1 // shift left x
     add 4 4 4 // shift left c
     beq 0 0 loop
plus add 3 1 3
    beq 0 0 next
exit halt
one .fill 1
mcand .fill -3
mplier .fill -2
count .fill 4294967296 // 2^32