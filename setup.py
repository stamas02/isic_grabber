#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="isic_grabber",
    version="1.1.1",
    description="Downloads the ISIC Archive",
    long_description=readfile('README.md'),
    author="Tamas Suveges",
    author_email="stamas01@gmail.com",
    url="",
    packages=['isic_grabber', 'isic_grabber.src', 'isic_grabber.data'],
    include_package_data=True,
    license=readfile('LICENSE'),
    install_requires=[
        'tqdm',
        'pyfiglet',
        'click',
        'pandas',
        'requests'
   ],
    entry_points={
        'console_scripts': [
            'ls_isic = isic_grabber.list_isic:main',
            'grab_isic = isic_grabber.grab_isic:main'
        ]
    },
)