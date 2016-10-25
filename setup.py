#!/usr/bin/env python

PROJECT = 'kidsclient'

VERSION = '0.1'

from setuptools import setup,find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,
    description='kids client try',
    long_description=long_description,
    author='zdt',
    author_email='detongchang@gmail.com',
    url='https://github.com/tbbrave/python-kidsclient',
    download_url='https://github.com/tbbrave/python-kidsclient/tarball/master',
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                ],
    palforms=['Any'],
    scripts=[],
    providers=[],
    install_requires=['kidsclient'],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'kids = kiesclient.main: main'
        ],
        'kids.client': [
            'simple = kidsclient.simple: Simple',
            'error = kidsclient.simple: Error',
            'files = kidsclient.list: Files',
            'show file = kidsclient.show: File',
            'file = kidsclient.show: File',
            'show files = kidsclient.list: Files',
        ],
    },
    zip_safe=False,
)
