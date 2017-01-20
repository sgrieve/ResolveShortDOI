import requests
import json
import sys


def ShortDOI2URL(shortdoi):
    '''
    Convert a short doi into a url. No testing of validity of doi. Strips the
    prefix "10/" as it is not needed to resolve a url. I think.
    '''
    return ('doi.org/{0}').format(shortdoi[3:])


def ResolveShortDOI(doi):
    '''
    Pass a long doi through the shortdoi service and return the short doi as
    a string.
    '''
    URL = 'http://shortdoi.org/{0}?format=json'.format(doi)
    r = requests.get(URL)
    j = json.loads(r.text)

    return j['ShortDOI']
