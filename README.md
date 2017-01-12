## MagicGoogle

### 1.What's MagicGoogle
This is a simple google search results crawler


### 3.How to Use?
Run
``` shell
git clone https://github.com/howie6879/MagicGoogle.git
cd MagicGoogle
vim google_search.py
# Or 
python setup.py install
```
Coding
``` python
mg = MagicGoogle()
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

