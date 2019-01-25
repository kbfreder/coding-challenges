

def ScaleBalancing(strArr): 
    import numpy as np
    import random
    import math
    
    balArr = []
    wtArr = []
    
    balArr = strArr[0].split(",")
    balArr[0] = int(balArr[0].lstrip("["))
    balArr[1] = int(balArr[1].rstrip("]"))
    
    wtArr = strArr[1].split(",")
    for i in range(len(wtArr)):
        wtArr[i] = int(wtArr[i].lstrip("[").rstrip("]"))
    wtArr = [0,0] + wtArr
    
    success = False

    for i, w1 in enumerate(wtArr):
        red_wtArr = wtArr[:i] + wtArr[(i+1):]
        for w2 in red_wtArr:
            if (balArr[0] + w1 + w2 == balArr[1]) or (balArr[0] + w1 == balArr[1] + w2) or (balArr[0] + w2 == balArr[1] + w1) or (balArr[0] == balArr[1] + w1 + w2):
                if w1 !=0 and w2 != 0:
                    return ",".join([str(w1),str(w2)])
                elif w1 ==0:
                    return str(w2)
                elif w2 ==0:
                    return str(w1)
                success = True
                break

    
    if not success:
        return ("not possible")
    
return ",".join([str(w1),str(w2)])