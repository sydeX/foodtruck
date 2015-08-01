from utilities.utils import haversine


class FoodTruck(object):

    def __init__(self, name, fooditems, address, latitude, longitude):
        self.name = name
        self.fooditems = fooditems
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.distance = None

    # def _populateLatLng(self):
    #     '''
    #         Convert address to latlng coordinate if they are not specified
    #         very slow as a lot of trucks are missing coords, can be enabled when preloading data to DB
    #     '''
    #     if not self.hasLocation():
    #         if self.address:
    #             try:
    #                 self.latitude, self.longitude = getCoordByAddress(self.address).values()
    #             except:
    #                 logging.warning("No location information found for truck %s" % self.name)
    #         else:
    #             logging.warning("No location information found for truck %s" % self.name)

    def has_location(self):
        return self.latitude and self.longitude

    def compute_distance_from_coords(self, destlat, destlng):
        '''
        Calculate distance between the food truck and desitnation
        Update distance attribute with the calculated result

        :param destLat: destination latitude
        :type destLat: float or float in string format
        :param destLng: destination longitude
        :type destLng: float or float in string format
        '''
        if not self.has_location():
            return

        dist = haversine(float(self.longitude), float(self.latitude), float(destlng), float(destlat))
        self.distance = round(dist, 2)

    def to_dict(self):
        return self.__dict__
