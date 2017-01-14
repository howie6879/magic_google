import os
import sys
import random
import pprint

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MagicGoogle import MagicGoogle

PROXIES = [{
    'http': '192.168.2.207:1080',
    'https': '192.168.2.207:1080'
}]

mg = MagicGoogle(PROXIES)

for key, value in enumerate(range(10000)):
    try:
        print(key)
        sleep = random.randint(2, 15)
        pprint.pprint(list(mg.search_url(query='python', pause=sleep)))
    except Exception as e:
        print(e)
        pass
