def hacker_str_to_int_list(dinput):
    dinput = dinput.split()    
    for i in range(len(dinput)):
        dinput[i] = int(dinput[i])
    return dinput