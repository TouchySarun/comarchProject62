from my_utils import to_binary_str, binary_str_to_decimal, check_offset_field, check_isregister

#add binary
def addBinary(x, y): 
        max_len = max(len(x), len(y)) 
  
        x = x.zfill(max_len) 
        y = y.zfill(max_len) 
        result = ''       
        carry = 0
  
        for i in range(max_len - 1, -1, -1): 
            c = carry
            if x[i]=='1':c+=1
            else: c+=0

            if y[i]=='1':c+=1
            else:c+=0 

            if c%2==1: result = '1'+result
            else: result = '0'+result

            if c < 2:carry = 0 
            else: carry=1    
          
        if carry !=0:result = '1' + result 
  
        return result.zfill(max_len) 


#two complement
def twoCom(num):
    leng=len(num)
    oneCom=''
    count=0
    while count<leng:
        if int(num[count])==0:
            oneCom+='1'
        elif int(num[count])==1:
            oneCom+='0'
        count+=1
    return addBinary(oneCom,'1')



#main 
inputCommand=input("command: ")
data=inputCommand.split()  

label = str(data[0])
instruction = str(data[1])
field0 = int(data[2]) #regA
field1 = int(data[3]) #regB
field2 = int(data[4]) #offsetField
comments = str(data[5])


if check_isregister(field0) or check_isregister(field1):
elif check_offset_field(field2):
else:
    code="0000000"

    if instruction=="lw":
        code+="010"
    elif instruction=="sw":
        code+="011"
    elif instruction=="beq":   
        code+="100"

    binaryField0 = to_binary_str(binaryField0, 3)
    binaryField1 = to_binary_str(binaryField1, 3)

    code+=binaryField0
    code+=binaryField1

    if field2>=0:
        binaryField0 = to_binary_str(binaryField2, 16)
        code+=binaryField2
    else:
        field2*=-1
        binaryField0 = to_binary_str(binaryField2, 16)
        code+=twoCom(binaryField2)

    print("machine code is: ",code)
    print("value is: ",int(code, 2))

