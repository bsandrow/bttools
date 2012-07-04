
from collections import namedtuple, defaultdict

MagnetParam = namedtuple('MagnetParam', ['key', 'value'])

class MagnetUriError(Exception):
    pass

def is_valid_magnet_uri(uri):
    return uri.startswith('magnet:?')

def magnet_uri_split(uri):
    if not is_valid_magnet_uri(uri):
        raise MagnetUriError("Not a valid magnet uri: %s" % uri)

    magnet = {}
    magnet['scheme'], params_string = uri.split(':?')
    magnet['params'] = [ MagnetParam(*pair.split('=')) for pair in params_string.split('&') ]

    return magnet

class ParamDict(object):
    """
    ParamDict
    ~~~~~~~~~
    A dictionary-like object for storing query parameters from URLs.

    :params: A defaultdict of lists.
    """
    params = defaultdict(list)

    def __init__(self, params):
        if isinstance(params, basestring):
            params = [ tuple(*pair.split('=')) for pair in params.split('&') ]

        if isinstance(params, list):
            for k,v in params:
                self.params[k].append(v)
        else:
            raise ValueError("ParamDict only takes a string or a list of tuples")

    def get_one(self, name):
        """ Return only the first value for the param. """
        val = self.params[name]
        return val[0] if len(val) > 0 else None

    def get_all(self, name):
        """ Return a list of all values for the param key. """
        return self.params[name]

class MagnetUriParams(ParamDict):
    long_names = {
        'acceptable_source': 'as',
        'display_name'     : 'dn',
        'exact_length'     : 'xl',
        'exact_topic'      : 'xt',
        'exact_source'     : 'xs',
        'keyword_topic'    : 'kt',
        'manifest_topic'   : 'mt',
        'tracker'          : 'tr',
    }

    def keys(self, long_names=False):
        keys = self.params.keys()
        if long_names:
            return [ k for k,v in self.long_names.iteritems() if v in keys ]
        else:
            return keys

    def get_one(self, name):
        if name in long_names:
            name = self.long_names[name]
        val = self.params[name]
        if len(val) > 0:
            return val[0]
        else:
            return None

    def get_all(self, name):
        if name in self.long_names:
            name = self.long_names[name]
        return self.params[name]

class MagnetURI(object):
    magnet_uri = None
    params     = None

    def __init__(self, uri):
        self.magnet_uri = magnet_uri_split(uri)
        self.params = MagnetUriParams(self.magnet_uri['params'])

    @property
    def trackers(self):
        return self.params.get_all('tr')

