import logging

from utilities.utils import haversine, getCoordByAddress

class FoodTruck(object):

    # Maps Food truck attribute to SF open data fields
    ATTRIBUTE_MAP = {
        'applicant':'applicant',
        'fooditems':'fooditems',
        'address'  :'address',
        'latitude' :'latitude',
        'longitude': 'longitude',
        'distance' : None,
    }

    def __init__(self, attributes={}):
        '''
        Initialize all attributes defined in ATTRIBUTE_MAP
        :param attributes: dictionary
        :return: None
        '''


        for truckAttr, srcAttr in self.ATTRIBUTE_MAP.iteritems():
            if attributes and attributes.has_key(srcAttr):
                self.__setattr__(truckAttr, attributes.get(srcAttr))
            else:
                logging.warning("Missing truck attribute: %s" % truckAttr)
                self.__setattr__(truckAttr, None)

        #TODO: very slow as a lot of trucks are missing coords, can be enabled when preloading data to DB
        #self._populateLatLng()

    def _populateLatLng(self):
        '''
            Convert address to latlng coordinate if they are not specified
        '''
        if not self.hasLocation():
            if self.address:
                try:
                    self.latitude, self.longitude = getCoordByAddress(self.address).values()
                except:
                    logging.warning("No location information found for truck %s" % self.applicant)
            else:
                logging.warning("No location information found for truck %s" % self.applicant)

    def hasLocation(self):
        return self.latitude and self.longitude

    def updateDistance(self, destLat, destLng):
        '''
        Calculate distance between the food truck and desitnation
        Update distance attribute with the calculated result

        :param destLat: destination latitude
        :type destLat: float or float in string format
        :param destLng: destination longitude
        :type destLng: float or float in string format
        '''
        if not self.hasLocation():
            return

        dist = haversine(float(self.longitude), float(self.latitude), float(destLng), float(destLat))
        self.distance = round(dist,2)

    def toDict(self):
        return self.__dict__






