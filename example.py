# example.py
""" 
exampl.py (UUID)
to show off some features from cute `deploy`
"""
from rich import print 

log = print 
log(f'starting {__file__}')


def main( ):
    status = 'ok'
    log(f'in {__name__}')

    return status

result  = main()

log(f'finished {__file__}')

