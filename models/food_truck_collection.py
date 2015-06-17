from utilities.utils import loadURL, getCoordByAddress
from models.food_truck import FoodTruck

import logging

class FoodTruckCollection(object):

    def __init__(self, trucklist=[]):
        self.trucks = trucklist

    def addTruck(self, truck):
        self.trucks.append(truck)

    @staticmethod
    def createfromURL(url):
        res = []
        data = loadURL(url)

        for params in data:
            ft = FoodTruck(params)
            if ft.hasLocation():
                res.append(ft)

        return FoodTruckCollection(res)

    def getTruckData(self, address=None, toJson=True):
        '''
        :return: Map center coordinates, list of food truck data
        '''

        resDict = {'status': 'OK'}
        jsonizedTrucks = []

        try:
            logging.info("*************** " + str(address))
            addrCoord = getCoordByAddress(address)
            logging.info("*************** " + str(addrCoord))
            resDict['mapcenter'] = addrCoord

            for truck in self.trucks:
                truck.updateDistance(addrCoord['lat'], addrCoord['lng'])
                jsonizedTrucks.append(truck.toDict())

            resDict['trucks'] = jsonizedTrucks if toJson else self.trucks

        except Exception as e:
            logging.error(e.message)
            resDict = {'status': e.message }

        return resDict
