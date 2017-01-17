import os
import sys
import random
import unittest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MagicGoogle import MagicGoogle


class TestMagicGoogle(unittest.TestCase):
    """
    Test MagicGoogle class
    """

    def setUp(self):
        PROXIES = [{
            'http': '192.168.2.207:1080',
            'https': '192.168.2.207:1080'
        }]
        self.mg = MagicGoogle(PROXIES)

    def tearDown(self):
        self.mg = None

    def test_search_url(self):
        sleep = random.randint(2, 15)
        result = list(self.mg.search_url(query='python', num=1, pause=sleep))
        self.assertEqual(result[0], 'https://www.python.org/', 'test search_url fail')


if __name__ == '__main__':
    unittest.main()
