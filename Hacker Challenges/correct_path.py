
def CorrectPath(str): 
    import numpy as np
    import random
    

    move_dict = {'d':[1,0], 'u':[-1,0], 'r':[0,1], 'l':[0,-1]}
    
    while True:
        route = []
        m = np.zeros((5,5))
        m[0,0] = 1
        r,c = [0,0]
        check = 0
        for s in str:
            if s == '?': s = random.choice('urdl')
            
            dr,dc = move_dict[s]
            r, c = r+dr, c+dc
            
            try:
                if m[r,c] == 1:
                    check = 0
                    break
                else: 
                    check = 1
                    route.append(s)
                    #print (route)
                    m[r,c] = 1
            except:
                break
            
            if r==4 and c==4 and check==1:
                #print ("Final route: ")
                return "".join(route)
            
            
def CorrectPath_alt(str): 
    import numpy as np
    import random
    

    move_dict = {'d':[1,0], 'u':[-1,0], 'r':[0,1], 'l':[0,-1]}
    
    while True:
        route = []
        m = np.zeros((5,5))
        m[0,0] = 1
        r,c = [0,0]
        check = 0
        for s in str:
            if s == '?': s = random.choice('urdl')
            
            dr,dc = move_dict[s]
            r, c = r+dr, c+dc
            
            if r > 4 or c >4: break
            else:
                if m[r,c] == 1:
                    check = 0
                    break
                else: 
                    check = 1
                    route.append(s)
                    #print (route)
                    m[r,c] = 1
            
            if r==4 and c==4 and check==1:
                #print ("Final route: ")
                return "".join(route)