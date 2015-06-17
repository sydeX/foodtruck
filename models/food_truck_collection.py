from utilities.utils import loadURL, getCoordByAddress
from models.food_truck import FoodTruck

import logging

class FoodTruckCollection(object):

    def __init__(self, trucklist=[]):
        self.trucks = trucklist

    def addTruck(self, truck):
        self.trucks.append(truck)

    def __len__(self):
        return len(self.trucks)

    @staticmethod
    def createfromURL(url):
        res = []
        data = loadURL(url)

        if data != None:
            for params in data:
                ft = FoodTruck(params)
                if ft.hasLocation():
                    res.append(ft)
        else:
            logging.warning("No data returned from URL %s" % url)

        return FoodTruckCollection(res)

    def getTruckData(self, address=None, toJson=True):
        '''
        :return: Map center coordinates, list of food truck data
        '''

        resDict = {'status': 'OK'}
        jsonizedTrucks = []

        try:
            addrCoord = getCoordByAddress(address)
            resDict['mapcenter'] = addrCoord

            for truck in self.trucks:
                truck.updateDistance(addrCoord['lat'], addrCoord['lng'])
                jsonizedTrucks.append(truck.toDict())

            resDict['trucks'] = jsonizedTrucks if toJson else self.trucks

        except Exception as e:
            logging.error(e.message)
            resDict = {'status': e.message }

        return resDict
