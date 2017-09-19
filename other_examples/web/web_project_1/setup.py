try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Ricardo A',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ricardo@enmotionvalue.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['web1'],
    'scripts': [],
    'name': 'web1'
}

setup(**config)
