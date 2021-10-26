from setuptools import setup

setup(
  name='twty',
  version='0.1.0',
  py_modules=['__init__'],
  install_requires=[
      'Click',
      'Tweepy'
  ],
  entry_points={
      'console_scripts': [
          '__init__ = __init__:cli',
      ],
  },
)