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

for i in mg.search_url(query='python', pause=3):
    pprint.pprint(i)


exit()
for key, value in enumerate(range(10000)):
    print(key)
    sleep = random.randint(2, 30)
    for i in mg.search_url(query='python', pause=sleep):
        pprint.pprint(i)
