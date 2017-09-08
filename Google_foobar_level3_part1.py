# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:01:38 2017

@author: ning
"""
def quick_xor(end):
    result = [end, 1, end + 1, 0]
    return result[end%4]

def answer(start, length):
    checksum = 0
    skip = 0
    s = start
    while skip < length:
        temp = quick_xor(s-1)^quick_xor(s+length - skip - 1)
        #print temp
        checksum = checksum ^ temp
        #print checksum
        s = s + length
        skip += 1
    return checksum
    
    
    
print answer(0, 100000)
    
    
    
    
"""   
    line = range(start, start + length)
    skip = 0
    checked = []
    while skip < length:
        checked += line[:(length - skip)]
        skip += 1
        line = range(line[length - 1] + 1, line[length - 1] + 1 + length)
    checksum = checked[0]
    for i in xrange(1,len(checked)):
        checksum = checksum ^ checked[i]
    return checksum
 """  


#print answer(0, 100000)4352462848