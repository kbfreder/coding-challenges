#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:52:39 2019

@author: kendra
"""

"""
From: Programming Interviews Exposed
"""


'''Implement binary search on sorted array to find the index of an integer'''


'''Telephone words:
    find all "words" (or non-sensical combination of letters) that can 
    represent the given telephone number
    Assume only valid phone numbers passed
'''

def helper(tel_key, place):
    tel_key_dict = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'],
                    5:['J','K','L'], 6:['M','N','O'], 7:['P','R','S'],
                    8:['T','U','V'], 9:['W','X','Y']}
    

def tel_words(num):