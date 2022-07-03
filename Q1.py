def dec_to_bin(n):
    n=int(n)
    z=""
    if n==0:
        z=z+"0"
    else:
        while n>0:
            y=n%2
            n=n//2
            z=z+str(y)
    if len(z)!=8:
        z=z+"0"*(8-len(z))
    return z[::-1]

lc=0
label_dict={}
var_dict={}
with open("project.txt","r") as f:
    data=f.read().split("\n")
    var_counter=0
    for i in data:
        if(i.split()[0]=="var"):
            var_counter=var_counter+1
mem_counter=len(data)-var_counter



with open("project.txt","r") as f:
    data=f.read().split("\n")
    flag=False
    var_counter=0
    for i in data:
        if(i.split()[0]=="var"):
            var_dict[i.split()[1]]=mem_counter
            mem_counter=mem_counter+1

dict={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
with open("project.txt","r") as f:
    data=f.read().split("\n")
    flag=False
    for i in data:

        if i.split()[0]=="mov" and i.split()[2][0]=="$":
            y=dict[i.split()[1]]
            z=i.split()[2][1:]
            lc=lc+1
            print("10010"+y+dec_to_bin(z))

        if i.split()[0]=="mov" and i.split()[2][0]!="$":
            lc=lc+1
            print("10011"+"00000"+dict[i.split()[1]]+dict[i.split()[2]])

        elif i.split()[0]=="add":
            lc=lc+1
            print("10000"+"00"+dict[i.split()[1]]+dict[i.split()[2]]+dict[i.split()[3]])

        elif i.split()[0]=="sub":
            lc=lc+1
            print("10001"+"00"+dict[i.split()[1]]+dict[i.split()[2]]+dict[i.split()[3]])

        elif i.split()[0]=="mul":
            lc=lc+1
            print("10110"+"00"+dict[i.split()[1]]+dict[i.split()[2]]+dict[i.split()[3]])

        elif i.split()[0]=="div":
            lc=lc+1
            print("10111"+"00000"+dict[i.split()[1]]+dict[i.split()[2]])

        elif i.split()[0]=="ls" and i.split()[2][0]=="$":
            z=i.split()[2][1:]
            lc=lc+1
            print("11001"+dict[i.split()[1]]+dec_to_bin(z))

        elif i.split()[0]=="rs" and i.split()[2][0]=="$":
            z=i.split()[2][1:]
            lc=lc+1
            print("11000"+dict[i.split()[1]]+dec_to_bin(z))

        elif i.split()[0]=="or":
            lc=lc+1
            print("11011"+"00"+dict[i.split()[1]]+dict[i.split()[2]]+dict[i.split()[3]])

        elif i.split()[0]=="and":
            lc=lc+1
            print("11100"+"00"+dict[i.split()[1]]+dict[i.split()[2]]+dict[i.split()[3]])

        elif i.split()[0]=="not":
            lc=lc+1
            print("11100"+"00000"+dict[i.split()[1]]+dict[i.split()[2]])

        elif i.split()[0]=="cmp":
            lc=lc+1
            print("11110"+"00000"+dict[i.split()[1]]+dict[i.split()[2]])

        elif i.split()[0]=="xor":
            lc=lc+1
            print("11010"+"00"+dict[i.split()[1]]+dict[i.split()[2]]+dict[i.split()[3]])

        elif i.split()[0]=="ld":
            lc=lc+1
            print("10100"+dict[i.split()[1]]+dec_to_bin(str(var_dict[i.split()[2]])))

        elif i.split()[0]=="st":
            lc=lc+1
            print("10101"+dict[i.split()[1]]+dec_to_bin(str(var_dict[i.split()[2]])))

        elif i.split()[0]=="jmp":
            lc=lc+1
            print("11111"+"000"+str(dec_to_bin(label_dict[i.split()[1]])))

        elif i.split()[0]=="jlt":
            lc=lc+1
            print("01100"+"000"+str(dec_to_bin(label_dict[i.split()[1]])))

        elif i.split()[0]=="jgt":
            lc=lc+1
            print("01101"+"000"+str(dec_to_bin(label_dict[i.split()[1]])))

        elif i.split()[0]=="je":
            lc=lc+1
            print("01111"+"000"+str(dec_to_bin(label_dict[i.split()[1]])))

        elif i.split()[0]=="hlt":
            lc=lc+1
            print("01010"+"00000000000")
            break

        elif i.split()[0][-1]==":":
            label_dict[i.split()[0][:-1]]=lc
            lc=lc+1
 
            if i.split()[1]=="mov" and i.split()[3][0]=="$":
                y=dict[i.split()[2]]
                z=i.split()[3][1:]
                print("10010"+y+dec_to_bin(z))

            if i.split()[1]=="mov" and i.split()[3][0]!="$":
                print("10011"+"00000"+dict[i.split()[2]]+dict[i.split()[3]])

            elif i.split()[1]=="add":
                print("10000"+"00"+dict[i.split()[2]]+dict[i.split()[3]]+dict[i.split()[4]])

            elif i.split()[1]=="sub":
                print("10001"+"00"+dict[i.split()[2]]+dict[i.split()[3]]+dict[i.split()[4]])

            elif i.split()[1]=="mul":
                print("10110"+"00"+dict[i.split()[2]]+dict[i.split()[3]]+dict[i.split()[4]])

            elif i.split()[1]=="div":
                print("10111"+"00000"+dict[i.split()[2]]+dict[i.split()[3]])

            elif i.split()[1]=="ls" and i.split()[3][0]=="$":
                z=i.split()[3][1:]
                print("11001"+dict[i.split()[2]]+dec_to_bin(z))

            elif i.split()[1]=="rs" and i.split()[3][0]=="$":
                z=i.split()[3][1:]
                print("11000"+dict[i.split()[2]]+dec_to_bin(z))

            elif i.split()[1]=="or":
                print("11011"+"00"+dict[i.split()[2]]+dict[i.split()[3]]+dict[i.split()[4]])

            elif i.split()[1]=="and":
                print("11100"+"00"+dict[i.split()[2]]+dict[i.split()[3]]+dict[i.split()[4]])

            elif i.split()[1]=="not":
                print("11100"+"00000"+dict[i.split()[2]]+dict[i.split()[3]])

            elif i.split()[1]=="cmp":
                print("11110"+"00000"+dict[i.split()[2]]+dict[i.split()[3]])

            elif i.split()[1]=="xor":
                print("11010"+"00"+dict[i.split()[2]]+dict[i.split()[3]]+dict[i.split()[4]])

            elif i.split()[1]=="ld":
                print("10100"+dict[i.split()[2]]+dec_to_bin(str(var_dict[i.split()[3]])))

            elif i.split()[1]=="st":
                print("10101"+dict[i.split()[2]]+dec_to_bin(str(var_dict[i.split()[3]])))

            elif i.split()[1]=="jmp":
                print("11111"+"000"+str(dec_to_bin(label_dict[i.split()[2]])))

            elif i.split()[1]=="jlt":
                print("01100"+"000"+str(dec_to_bin(label_dict[i.split()[2]])))

            elif i.split()[1]=="jgt":
                print("01101"+"000"+str(dec_to_bin(label_dict[i.split()[2]])))

            elif i.split()[1]=="je":
                print("01111"+"000"+str(dec_to_bin(label_dict[i.split()[2]])))

            elif i.split()[1]=="hlt":
                print("01010"+"00000000000")
                break


print(lc)
print(var_dict)
print(label_dict)

