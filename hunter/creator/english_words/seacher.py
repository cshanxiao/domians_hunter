# -*- coding: utf-8 -*-
u'''
@summary: http://www.wordcount.org/main.php
@author: cshanxiao
@date: 2017-04-13
'''

import requests
import string
import threading
import time
import traceback
import urlparse
import urllib
url_tpl = "http://www.wordcount.org/dbquery.php?toFind={}&method=SEARCH_BY_INDEX"
lock = threading.Lock()

class WordsClass(object):

    def __init__(self):
        '''
        Constructor
        '''

def check_domian(url):
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            print urlparse.parse_qs(resp.content)
    except:
        traceback.print_exc()

if __name__ == '__main__':

    threads = []
    for i in xrange(90000):
        url = url_tpl.format(i)
        t1 = threading.Thread(target=check_domian, args=(url,))
        threads.append(t1)

        if len(threads) > 8:
            for t in threads:
                t.setDaemon(True)
                time.sleep(1)
                t.start()

            for t in threads:
                t.join()

            threads = []
            time.sleep(2)

