from setuptools import setup

setup(
  name='twty',
  version='0.1.0',
  py_modules=['twty'],
  install_requires=[
      'Click',
      'Tweepy'
  ],
  entry_points={
      'console_scripts': [
          'twty = twty:cli',
      ],
  },
)