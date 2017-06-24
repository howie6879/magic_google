## MagicGoogle

### 1.What's MagicGoogle
This is an easy Google Seraching crawler that you can get anything you want in the page by using it.

During the process of  crawling,you need to pay attention to the limitation from google towards ip address and the warning of exception , so I suggest that you should pause running the program and own the Proxy ip

php - [MagicGoogle](https://github.com/howie6879/phpGoogle)

### 2.How to Use?
Run
``` shell
pip install MagicGoogle
# Or
git clone https://github.com/howie6879/MagicGoogle.git
cd MagicGoogle
vim google_search.py
# Or 
python setup.py install
```
Example
``` python
from MagicGoogle import MagicGoogle
import pprint

# Or PROXIES = None
PROXIES = [{
    'http': 'http://192.168.2.207:1080',
    'https': 'http://192.168.2.207:1080'
}]

# Or MagicGoogle()
mg = MagicGoogle(PROXIES)

#  Crawling the whole page
result = mg.search_page(query='python')

# Crawling url
for url in mg.search_url(query='python'):
    pprint.pprint(url)
    
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
```
You can see [google_search.py](./Examples/google_search.py)

**If  you need a big amount of querie but only having an ip address,I suggest  you can have a time lapse between 5s ~ 30s.**

The reason that it always return empty might be as follows:

```html
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="https://ipv4.google.com/sorry/index?continue=https://www.google.me/s****">here</A>.
</BODY></HTML>
```



