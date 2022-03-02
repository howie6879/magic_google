#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='magic_google',
    version='0.3.1',
    description="A google search results crawler",
    install_requires=['pyquery>=1.2.17', 'requests>=2.12.4', 'cchardet'],
    author='Howie Hu',
    author_email='xiaozizayang@gmail.com',
    url="https://github.com/howie6879/MagicGoogle/blob/master/README.md",
    packages=find_packages(),
    package_data={'MagicGoogle': ['data/*.txt']},
)
