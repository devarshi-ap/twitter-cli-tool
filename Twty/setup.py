#setup.py

from setuptools import setup

setup(
    name='twty',
    version='0.0.1',
    py_modules=['twty'],
    install_requires=[
      'Click',
      'Tweepy'
    ],
    entry_points={
        'console_scripts': [
            'twty=twty:cli'
        ]
    }
)