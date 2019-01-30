# -*- coding: utf-8 -*-

'''
Given A students in class, each assigned an id, 1 --> A, professor 
sorts them as if their IDs were strings
ex: 1, 10, 11, 12, 2, 3, 4, ... 9
and then chooses the IDs indicated by the indices in list B
(B is a 1-indexed list)
'''

def solve(self, A, B):
    strA = [str(a) for a in range(1,A+1)]
    strA.sort()
    rollcall = [strA[b-1] for b in B]
    return rollcall


def test(A):
    ''' '''
    ord_str_list = []
    for a in range(1,A+1):
        str_a = str(a)
        i = int(str_a[0])
        j = int(str_a[-1])
        l = len(str_a) # analogous to log-10 of a
        ins_pos = j-1 + l-1 + 10**(i-1)
        ord_str_list.insert(ins_pos , a)
    print(ord_str_list[:15])

def test4(A):
    '''works up to 99'''
    strA = []
    for a in range(1,A+1):
        i = int(str(a)[0])
        j = int(str(a)[-1])
        l = len(str(a)) - 1
        strA.insert((i-1)*10 + i*l + (j-1) + l, a)
    print(strA[:15])


def test3(A):
    '''works up to 19'''
    strA = []
    for a in range(1,A+1):
        i = int(str(a)[0])
        j = int(str(a)[-1])
        l = len(str(a)) - 1
        strA.insert(i*l + (j-1) + l, a)
    print(strA)
    #rollcall = [strA[b-1] for b in B]
    #return rollcall




def old_test(A, B, verbose=False):
    '''this works, but is too slow'''
    strA = [[] for _ in range(9)]
    for a in range(1, A+1):
        i = int(str(a)[0])
        strA[i-1].append(a)
    if verbose:
        print(strA)
    flatA = [y for x in strA for y in x]
    rollcall = [flatA[b-1] for b in B]
    return rollcall




def first_digit(M):
    return str(M)[0]

def test2(A):
    strA = [[] for _ in range(9)]
    for a in range(1, A+1):
        i = int(str(a)[0])
        print(i)
        strA[i-1].append(a)
        print(strA)
    
    return strA