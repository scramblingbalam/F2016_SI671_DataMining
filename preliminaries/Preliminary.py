# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:50:13 2016

@author: scram
"""

from collections import Counter
def doit(inum):
    if (inum == 0) : 
        return 1 
    return doit(inum - 1) * inum
    
print doit(4)

def dothat(inum):
    print "INUM  ",inum
    if (inum == 0) : 
        return 1
    that = dothat(inum-1) * (inum)
    print "that ==",that
    return that
print dothat(4),"\n"


'''
Q.8. Write a program to find the five character-level trigrams 
(strings with three characters, such as "abc" or "rey") 
that appear the highest number of times in the following poem 
(“When You Are Old” by W. B. Yeats). Please lowercase all letters. 
The trigrams should not contain spaces, but may include punctuations. 
The result should list the top five trigrams and how many times they occur, 
in the decreasing order of the occurrence frequency.
'''

poem = """When you are old and grey and full of sleep,
And nodding by the fire, take down this book,
And slowly read, and dream of the soft look
Your eyes had once, and of their shadows deep;
How many loved your moments of glad grace,
And loved your beauty with love false or true,
But one man loved the pilgrim soul in you,
And loved the sorrows of your changing face;
And bending down beside the glowing bars,
Murmur, a little sadly, how Love fled
And paced upon the mountains overhead
And hid his face amid a crowd of stars.
Paste your script and result. If you make any assumptions, write them down too."""




poem = poem.lower().replace("\n"," ")
print poem[-10:]
count = Counter("".join(i) for i in zip(poem,poem[1:],poem[2:]) if " " not in i)
print count.most_common(5)

