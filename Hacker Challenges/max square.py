import numpy as np

def MaximalSquare(s): 
    
    m = np.zeros((len(s), len(s[0])))
    for i, r in enumerate(s):
        for j, c in enumerate(s[i]):
            m[i,j] = c
    tally =[]
    
    for sq in range(2,max(len(m),len(m[0]))):
        print ('square size: ' + str(sq))
        for r in range (0,len(m) - sq+1):
            for c in range(0,len(m[0])-sq+1):
                r_sum = np.sum(m[r:r+sq,c:c+sq])
                #print (r_sum)
                if r_sum == sq**2:
                    tally.append(r_sum)
                    print ('added to tally: ' + str(r) + str(c) + " = " + str(r_sum))
                    
    print(tally)
    return max(tally)


def matrix_from_string(s):
    m = np.array([[int(x) for x in line] for line in s])
    return m
    
    
def short_MaxSquare(strArr):
    rows = [range(i,j) for i in range(0, len(strArr)) for j in range(i+1, len(strArr)+1)]
    cols = [range(i,j) for i in range(0, len(strArr[0])) for j in range(i+1, len(strArr[0])+1)]
    sub_mat = [
                [strArr[i][j]  for i in r for j in c]  
                for r in rows for c in cols  
                    if len(c) == len(r) and 
                    sum([int(strArr[i][j]) for i in r for j in c]) == len(r) * len(c)
                ]
    answer = len(max(sub_mat, key = len))