import sys
data=sys.stdin.read().strip().split("\n")
print(data)
dict={"000":"R0","001":"R1","010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}

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
        z=z+"0"*(16-len(z))
    return z[::-1]

dict1={"R0":dec_to_bin(0b0000000000000000),"R1":dec_to_bin(0b00000000000000),"R2":dec_to_bin(0b000000000000000),"R3":dec_to_bin(0b000000000000000),"R4":dec_to_bin(0b000000000000000),"R5":dec_to_bin(0b000000000000000),"R6":dec_to_bin(0b000000000000000),"FLAGS":dec_to_bin(0b000000000000000)}
print(dict1["R0"])
print(dict1["R1"])


def dec_to_bin_pc(n):
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

def b_to_d(n):
    z=0
    y=str(n)[::-1]
    for i in range(0,len(y)):
        z=z+((int(y[i]))*(2**(i)))
    return z

c=len(data)
while(c>0):
    for i in data:
        if i[0:5]=="10000":
            dict1[dict[i[13:16]]]=dec_to_bin(b_to_d(dict1[dict[i[7:10]]])+ b_to_d(dict1[dict[i[10:13]]]))
            if(b_to_d(dict1[dict[i[13:16]]]))>(2**16)-1:
                dict1[dict[i[13:16]]]=dec_to_bin(2**16-1)
                dict1["FLAGS"]=dec_to_bin(8)
            else:
                dict1["FLAGS"]=dec_to_bin(0)
            print(str(dec_to_bin_pc(len(data)-c))+" "+str(dict1["R0"])+" "+str(dict1["R1"])+" "+str(dict1["R2"])+" "+str(dict1["R3"])+" "+str(dict1["R4"])+" "+str(dict1["R5"])+" "+str(dict1["R6"])+" "+str(dict1["FLAGS"]))
            c=c-1
        if i[0:5]=="01010":
            dict1["FLAGS"]=dec_to_bin(0)
            print(str(dec_to_bin_pc(len(data)-c))+" "+str(dict1["R0"])+" "+str(dict1["R1"])+" "+str(dict1["R2"])+" "+str(dict1["R3"])+" "+str(dict1["R4"])+" "+str(dict1["R5"])+" "+str(dict1["R6"])+" "+str(dict1["FLAGS"]))
            c=c-1
        if i[0:5]=="10001":
            dict1[dict[i[13:16]]]=dec_to_bin(b_to_d(dict1[dict[i[7:10]]])-b_to_d(dict1[dict[i[10:13]]]))
            if(b_to_d(dict1[dict[i[7:10]]]))<(b_to_d(dict1[dict[i[10:13]]])):
                dict1[dict[i[13:16]]]=dec_to_bin(0)
                dict1["FLAGS"]=dec_to_bin(8)
            else:
                dict1["FLAGS"]=dec_to_bin(0)
            print(str(dec_to_bin_pc(len(data)-c))+" "+str(dict1["R0"])+" "+str(dict1["R1"])+" "+str(dict1["R2"])+" "+str(dict1["R3"])+" "+str(dict1["R4"])+" "+str(dict1["R5"])+" "+str(dict1["R6"])+" "+str(dict1["FLAGS"]))
            c=c-1
        if i[0:5]=="10010":
            dict1["FLAGS"]=dec_to_bin(0)
            dict1[dict[i[5:8]]]=dec_to_bin(b_to_d(i[8:16]))
            print(str(dec_to_bin_pc(len(data)-c))+" "+str(dict1["R0"])+" "+str(dict1["R1"])+" "+str(dict1["R2"])+" "+str(dict1["R3"])+" "+str(dict1["R4"])+" "+str(dict1["R5"])+" "+str(dict1["R6"])+" "+str(dict1["FLAGS"]))
            c=c-1
        if i[0:5]=="10011":
            dict1["FLAGS"]=dec_to_bin(0)


    

        

