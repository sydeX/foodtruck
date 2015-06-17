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

    def __init__(self, attributes):

        # Initialize all attributes defined in ATTRIBUTE_MAP
        for truckAttr, srcAttr in self.ATTRIBUTE_MAP.iteritems():
            self.__setattr__(truckAttr, attributes.get(srcAttr, None))

        #TODO: very slow as a lot of trucks are missing coords, can be enabled when preloading data to DB
        #self._populateLatLng()

    def _populateLatLng(self):
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
        if not self.hasLocation():
            return

        dist = haversine(float(self.longitude), float(self.latitude), float(destLng), float(destLat))
        self.distance = round(dist,2)

    def toDict(self):
        return self.__dict__






