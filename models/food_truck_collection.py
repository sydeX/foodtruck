from utilities.utils import getCoordByAddress

import logging

class FoodTruckCollection(object):

    def __init__(self, trucklist=[]):
        self.trucks = trucklist

    def addTruck(self, truck):
        self.trucks.append(truck)

    def __len__(self):
        return len(self.trucks)


    def getTruckData(self, address=None, toJson=True):
        '''
        :return: Map center coordinates, list of food truck data
        '''

        resDict = {'status': 'OK'}
        jsonizedTrucks = []

        try:
            addrCoord = getCoordByAddress(address)
            resDict['mapcenter'] = addrCoord

            # Update distance for each truck
            for truck in self.trucks:
                truck.computeDistanceFromCoords(addrCoord['lat'], addrCoord['lng'])
                jsonizedTrucks.append(truck.toDict())

            resDict['trucks'] = jsonizedTrucks if toJson else self.trucks

        except Exception as e:
            logging.error(e.message)
            resDict = {'status': e.message }

        return resDict
