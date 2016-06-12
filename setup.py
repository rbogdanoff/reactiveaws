from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

config = {
    'description': 'Reactive AWS',
    'author': 'Ron Bogdanoff',
    'url': 'https://github.com/rbogdanoff/reactiveaws',
    'author_email': 'ron.bogdanoff@gmail.com',
    'version': '0.0.1',
    'packages': find_packages(exclude=('tests', 'docs')),
    'scripts': [],
    'name': 'rxaws',
    'license': license,
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'classifiers': [
         'Development Status :: 1 - Planning',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: Apache Software License',
         'Programming Language :: Python :: 3'
     ],
}

setup(**config)
