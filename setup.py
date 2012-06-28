from glob import glob

try:
    from setuptools import setup
except ImportError:
    print "Falling back to distutils. Functionality may be limited."
    from distutils.core import setup

config = {
    'description'  : 'Suite of command-line tools for dealing with BitTorrent files',
    'url'          : 'http://github.com/bsandrow/bttools',
    'author'       : 'Brandon Sandrowicz',
    'author_email' : 'brandon@sandrowicz.org',
    'version'      : '0.1',
    'packages'     : [],
    'scripts'      : glob('scripts/*'),
    'name'         : 'bttools',
    'test_suite'   : '',
}

setup(**config)
