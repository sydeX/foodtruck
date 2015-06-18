import logging
from models.food_truck import FoodTruck
from models.food_truck_collection import FoodTruckCollection
from utilities.utils import loadURL

class FoodTruckDataSource(object):
    APPLICANT = 'applicant'
    FOOD_ITEMS = 'fooditems'
    ADDRESS = 'address'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'

    URL = 'https://data.sfgov.org/resource/rqzj-sfat.json'
    ATTRIBUTE_FIELDS = [APPLICANT, FOOD_ITEMS, ADDRESS, LATITUDE, LONGITUDE]
    URL_BASIC_FITLER = '?status=APPROVED&$select=%s'% ','.join(filter(None, ATTRIBUTE_FIELDS))

    @staticmethod
    def getFoodTrucks():
        url = FoodTruckDataSource.URL + FoodTruckDataSource.URL_BASIC_FITLER

        res = []
        data = loadURL(url)

        if data != None:
            for params in data:

                attr_fields = []
                for field in FoodTruckDataSource.ATTRIBUTE_FIELDS:
                    attr_fields.append(params.get(field, None))

                ft = FoodTruck(*attr_fields)
                if ft.hasLocation():
                    res.append(ft)
        else:
            logging.warning("No data returned from URL %s" % url)

        return FoodTruckCollection(res)
