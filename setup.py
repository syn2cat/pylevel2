#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pylevel2',
    version='1.0',
    author='Raphaël Vinot',
    author_email='raphael.vinot@gmail.com',
    maintainer='Raphaël Vinot',
    url='https://github.com/Kaweechelchen/Level2.lu',
    description='Python API for Level2.',
    long_description=open('README.md').read(),
    packages=['pylevel2'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Internet',
    ],
    install_requires=['requests'],
)
