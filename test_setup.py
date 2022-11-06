""" 
test_setup.py (UUID)
use cookiecutter to generate a template for a python package
"""
from rich import print 

log = print 
log(f'starting {__file__}')
from cookiecutter.main import cookiecutter #|!md [docs](https://cookiecutter.readthedocs.io/en/stable/README.html)

if False: #| short version
    cookiecutter('cookiecutter-pypackage/')

else:           #| use url
    cookiecutter('https://github.com/audreyfeldroy/cookiecutter-pypackage.git')


