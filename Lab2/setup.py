try:
	from setuptools import setup

except ImportError:
	from distutils.core import setup

config = [
	'description': 'Game for lab1',
	'author': 'YOUR NAME',
	'url': 'TBD',
	'download_url': 'TBD',
	'author_email': 'CNET@uchicago.edu',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['game'],
	'scripts': [],
	'name': 'my_game'
]

setup(**config)