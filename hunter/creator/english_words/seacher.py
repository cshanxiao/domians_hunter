# -*- coding: utf-8 -*-
u'''
@summary: 英文单词词频前 200000
@author: cshanxiao
@date: 2017-04-13
'''

import requests
import threading
import time
import traceback
import urlparse

class Words(object):

    def __init__(self):
        self.words = []
        words = set()
        with open("./words_20k.txt") as fd:
            for line in fd.readlines():
                line = line.strip().lower()
                if not line or line.startswith("#") or line in words:
                    continue
                self.words.append(line)
                words.add(line)
        
    def get_words(self, start=0, end=100, length_lt=3):
        words = [item for item in self.words[start: end] if len(item) < length_lt]
        return words
    
def test():
    words = Words()
    wanted_words = words.get_words(end=2000000, length_lt=4)
    print len(wanted_words), ",".join(wanted_words)
    
if __name__ == '__main__':
    test()

