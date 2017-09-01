# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:00:12 2017

@author: ning
"""
def answer(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    reverse_letters = letters[::-1]
    letters_dict = {}
    for l, r in zip(letters, reverse_letters):
        letters_dict[l] = r
    translation = ""
    for letter in s:
        try:
            translation += letters_dict[letter]
        except:
            translation += letter

if __name__ == '__main__':
    #s = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    print answer(s)
