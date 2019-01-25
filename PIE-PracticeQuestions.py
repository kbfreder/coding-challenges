# -*- coding: utf-8 -*-
"""
From: Programming Interviews Exposed
"""


'''
Find the first non-repeated character in a string (p106)
Examples: 
    in = "total". out = "o"
    in = "teeter", out = "r"
'''


'''
Remove specified characters (p109)
function(str, remove): any character 'remove' is deleted from 'str'
return: str
note: keep spaces and punctuation
Example: "Battle of the Vowels", "aeiou" --> "Bttl f th Vwls"
'''


'''
Reverse order of words in a string (p112)
assume all words are space-delimited and treat punctuation as leter
Example: "Do or do not, there is no try." --> "try. no is there not, do or Do"
'''


'''
'''
def roll_two_dice():
    import numpy as np
    num = np.random.randint(0,35)
    die1 = num // 6 + 1
    die2 = num % 6 + 1
    return die1, die2
