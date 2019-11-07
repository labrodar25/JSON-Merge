from setuptools import setup
from setuptools import find_packages

setup(name='JSON-Merge',
      version='1.0',
      description='Merge JSON Files',
      author='Vijay Balaji',
      install_requires=[
                        'glob3',
                        'regex'
                        ],
      packages=find_packages())