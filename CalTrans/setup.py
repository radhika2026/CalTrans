from setuptools import setup, find_packages

setup(
    name='pems-api',
    version='0.1.0',
    description='A Python library for interacting with the CalTrans PeMS API',
    author='AAAAA',
    author_email='email@email.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'beautifulsoup4'
    ],
)