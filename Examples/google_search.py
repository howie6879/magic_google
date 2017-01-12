import os
import sys
import time
import random
import pprint
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MagicGoogle import MagicGoogle

################################################
# """
# cd MagicGoogle
# python Examples/search_result.py
# """
#################################################

PROXIES = [{
    'http': 'http://192.168.2.207:1080',
    'https': 'http://192.168.2.207:1080'
}]

# Or MagicGoogle()
mg = MagicGoogle(PROXIES)

# The first page of results
result = mg.search_page(query='python')
print(result)

time.sleep(random.randint(1, 3))

# Get url
for url in mg.search_url(query='python'):
    pprint.pprint(url)

time.sleep(random.randint(1, 3))

# Output
# 'https://www.python.org/'
# 'https://www.python.org/downloads/'
# 'https://www.python.org/about/gettingstarted/'
# 'https://docs.python.org/2/tutorial/'
# 'https://docs.python.org/'
# 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# 'https://www.codecademy.com/courses/introduction-to-python-6WeG3/0?curriculum_id=4f89dab3d788890003000096'
# 'https://www.codecademy.com/learn/python'
# 'https://developers.google.com/edu/python/'
# 'https://learnpythonthehardway.org/book/'
# 'https://www.continuum.io/downloads'

# Get {'title','url','text'}
for i in mg.search(query='python', num=1):
    pprint.pprint(i)
# Output
# {'text': 'The official home of the Python Programming Language.',
# 'title': 'Welcome to Python .org',
# 'url': 'https://www.python.org/'}
