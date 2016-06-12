from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

config = {
    'description': 'Reactive AWS',
    'author': 'Ron Bogdanoff',
    'url': 'https://github.com/rbogdanoff/reactiveaws',
    'author_email': 'ron.bogdanoff@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': find_packages(exclude=('tests', 'docs')),
    'scripts': [],
    'name': 'rxaws',
    'license': license
}

setup(**config)
