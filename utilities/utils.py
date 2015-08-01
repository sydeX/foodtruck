import json
import urllib2
import logging
from math import radians, cos, sin, asin, sqrt


def load_url(url):
    '''
    Load data from url which returns data in json format

    :param url: string
    :return: json
    '''

    return json.load(urllib2.urlopen(url))


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 3956  # Use 3956 for miles
    return c * r


def get_coord_by_address(addr):
    '''
        Use google geocode api to convert address to a dictionary of Lat Lng coordinates
    '''
    res = load_url('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % urllib2.quote(addr))
    if res['status'] == 'OK':
        return res['results'][0]['geometry']['location']
    else:
        logging.error("Failed looking up address %s, with status %s" % (addr, res['status']))
        raise Exception(res['status'])
