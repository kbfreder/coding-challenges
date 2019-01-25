# Complete the function below.
sym2num = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD': 400, 'D':500, 'CM':900, 'M': 1000}

num2sym = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X',40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}


# 260 ms, 15%
def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                 (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                 (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    
    for d, r in roman_map:
        factor = num // d
        if factor > 0:
            roman += factor * r
            num -= factor * d

    return roman


# this was slower than intToRoman3!
def intToRoman4(num):
    """
    :type num: int
    :rtype: str
    """
    roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                 (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                 (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    
    for d, r in roman_map:
        while num >= d and num > 0:
            roman += r
            num -= d

    return roman


# faster than intToRoman2
def intToRoman3(num):
    """
    :type num: int
    :rtype: str
    """
    roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                 (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                 (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    
    while num > 0:
        for d, r in roman_map:
            while num >= d:
                roman += r
                num -= d

        return roman



def intToRoman2(num):
    """
    :type num: int
    :rtype: str
    """
    divisors = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1, 0]
    numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    roman_list = []
    
    for i in range(len(divisors)-1):
        d = divisors[i]
        if num // d > 0:
            while num >= d:
                roman_list.append(numerals[i])
                num -= d
                print(num)

    return ''.join(roman_list)