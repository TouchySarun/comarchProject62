
lw x y z : y = mem[x+z]
sw x y z : mem[x+z] = y
add x y z : z = x+y
nand x y z : z = x nand y
beq x y z : jump to z if x = y
jalr x y : store pc+1 to y & jump to x

comb(n,r) = comb(n-1,r)+comb(n-1,r-1)
0 = 0 
1 = in
2 = in 
3 = out
4 = 
5 = sp
6 = 
7 = return addr

        lw	0	1	n
        lw	0	2	r
        lw 	0	4 	mone
        lw	0	3	one
        lw 	0	5	stack
	
comb	add	5	3	5
	    sw	0	7	5	    0(5) = 7
	
        lw	0	3	one
        beq	1	2	return
        beq	0	r	return
        add	0	1	3
        beq	3	2	return

        lw  0   4   mone
        add 1   4   1
        jalr7   comb        comb(n-1,r)
        add 0   3   6
        add 2   4   2       comb(n-1,r-1) 
        add 3   6   3
        jalr0 return

return	lw  0   4   mone
        add 5   4   5
        lw	0	7	5
        jalr 0  7

one     .fill   1
mone    .fill   -1
three   .fill   3
mthree  .fill   -3
	
