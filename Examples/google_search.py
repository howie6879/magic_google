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
    'http': 'http://127.0.0.1:8118',
    'https': 'http://127.0.0.1:8118'
}]

# Or MagicGoogle()
mg = MagicGoogle(PROXIES)

# The first page of results
# result = mg.search_page(query='python')
# print(result)
#
# time.sleep(random.randint(1, 5))

# Get {'title','url','text'}
for i in mg.search(query='python', num=1, language='en'):
    pprint.pprint(i)

time.sleep(random.randint(1, 5))

# Output
# {'text': 'The official home of the Python Programming Language.',
# 'title': 'Welcome to Python .org',
# 'url': 'https://www.python.org/'}

# Get first page
for url in mg.search_url(query='python'):
    pprint.pprint(url)

time.sleep(random.randint(1, 5))

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

# Get second page
for url in mg.search_url(query='python', start=10):
    pprint.pprint(url)

# Output
# 'https://github.com/python'
# 'https://github.com/python/cpython'
# 'https://www.learnpython.org/'
# 'https://www.raspberrypi.org/documentation/usage/python/'
# 'https://www.reddit.com/r/Python/'
# 'https://www.datacamp.com/courses/intro-to-python-for-data-science'
# 'https://www.coursera.org/learn/python'
# 'https://www.coursera.org/learn/interactive-python-1'
# 'http://abcnews.go.com/US/record-breaking-17-foot-python-captured-south-florida/story?id=51616851'
# 'https://hub.docker.com/_/python/'
