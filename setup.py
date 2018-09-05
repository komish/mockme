long_description = \
"""
A utility script to translate a phrase into a mockery version
of the same phrase.
"""

from setuptools import setup

def get_version():
    with open('VERSION', 'r') as f:
        x = f.read().splitlines()
        if len(x) == 1:
            return x[0]
        else:
            raise RuntimeError(
                'Cannot properly parse version information. '+
                'Parser found multiple versions where one was expected.')


setup(
    name='mockme',
    version=get_version(),
    description='Translate a phrase into mockery',
    long_description=long_description,
    url='https://github.com/komish/mockme',
    packages=['mockme'],
    author='Jose R. Gonzalez',
    author_email='Komish@users.noreply.github.com',
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': ['mockme=mockme.main:main']
    }
)
