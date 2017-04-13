import urllib
import string
import threading
import time
import traceback

letters = string.ascii_lowercase

chinese_shengmu = "b p m f d t n l g k h j q x zh ch sh r z c s y w"
chinese_yunmu = "a o e i u ai ei ui ao ou iu ie ue er an en in un ang eng ing ong"

url_tpl = "http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}"

domain_pres = [
    "i", "ai", "hao", "xi", "li", "bo", "bi", "pa", "pi", "pu", "bu", "ma",
    "mo", "mi", "mu", "fa", "da", "di"
]
domain_exts = [".com"]

def check_domian(url):
    try:
        req2 = urllib.urlopen(url)
        print req2.read()
        if "210" in req2.read().decode():
            print url
    except:
        traceback.print_exc()

if __name__ == '__main__':

    threads = []
    for sm in chinese_shengmu.split(" "):
        for ym in chinese_yunmu.split(" "):
            for ext in domain_exts:
                url = url_tpl.format("%s%s%s" % (sm, ym, ext))
                t1 = threading.Thread(target=check_domian, args=(url,))
                threads.append(t1)

                if len(threads) > 8:
                    for t in threads:
                        t.setDaemon(True)
                        time.sleep(0.5)
                        t.start()

                    for t in threads:
                        t.join()

                    threads = []
                    time.sleep(3)