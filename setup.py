from distutils.core import setup

setup(
    name='django_master_slave',
    version='1.0',
    packages=['database_routing'],
    url='https://github.com/just-work/django-database-routing',
    license='Apache License v2.0',
    author='tumbler',
    author_email='zimbler@gmail.com',
    description='''Provides master-slave routing
        and force master context manager for Django'''
)