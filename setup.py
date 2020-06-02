#!/usr/bin/python
# encoding: utf-8


from setuptools import setup, find_packages

setup(
    name="book_utils",
    version="0.1",
    license="MIT Licence",
    # urls ='https://github.com/bokunshu/sbook_package.git'
    url="https://github.com/bokunshu",
    author="sbk",
    author_email="shu_bk@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)