# -*- coding: utf-8 -*-
import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
install_requires = []
dependency_links = []
req_files = ['requirements.txt']

for file in req_files:
    with open(os.path.join(here, file)) as f:
        lines = f.readlines()
        install_requires.extend([p.strip() for p in lines if ' ' not in p])
        dependency_links.extend([p.split()[-1].strip() for p in lines
                                 if ' ' in p])

setup(
    name='spirit',
    description='',
    url='https://github.com/koalagogo/spirit',
    version='0.1.0',

    author='kolagogo org',
    author_email='',

    platforms='any',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    packages=find_packages('.', exclude=('tests*')),
    install_requires=install_requires,
    dependency_links=dependency_links,
)
