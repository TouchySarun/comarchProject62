    lw 	0	1	prd	
	lw	0	2	input	
	lw	0	3	fact
	lw	0	5	mc	
L1	lw	0	4	nandb	
	lw	0	7	exit
	add	3 	4	3	
	nand	3	4	6
	nand	6	6	6	
	beq	6	0	L2	
	add	5	1	1	
L2	add	5	5	5	
	add	4	4	4	
	beq	4	7	count	
	nand	3	4	6
	nand	6	6	6	 
	beq	6	0	L2	
	add	5	1	1	
	beq	0	0	L2	
count	add	1	0	5
	bep	2	3	end
	beq	0	0	L1
end	halt				
prd	.fill	0			
input	.fill	3			
fact	.fill	0			
nandb	.fill	1			
mc	.fill	1		
exit	.fill	4294967296	