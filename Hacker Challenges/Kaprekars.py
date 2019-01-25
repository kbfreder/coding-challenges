def KaprekarsConstant(n): 
    num = n
    r = 0
    while num != 6174:
        while len(str(num)) <4:
                num = int(str(num) + '0')
        desc = int("".join(sorted(str(num))))
        asc = int("".join(sorted(str(num),reverse=True)))
        num = asc-desc
        r +=1
    
    return r


# keep this function call here  
#print KaprekarsConstant(raw_input())  


