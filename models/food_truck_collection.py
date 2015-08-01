from utilities.utils import get_coord_by_address
import logging


class FoodTruckCollection(object):

    def __init__(self, trucklist=[]):
        self.trucks = trucklist

    def add_truck(self, truck):
        self.trucks.append(truck)

    def __len__(self):
        return len(self.trucks)

    def get_truck_data(self, address=None, to_json=True):
        '''
        :return: Map center coordinates, list of food truck data
        '''

        res_dict = {'status': 'OK'}
        jsonized_trucks = []

        try:
            addr_coord = get_coord_by_address(address)
            res_dict['mapcenter'] = addr_coord

            # Update distance for each truck
            for truck in self.trucks:
                truck.compute_distance_from_coords(addr_coord['lat'], addr_coord['lng'])
                jsonized_trucks.append(truck.to_dict())

            res_dict['trucks'] = jsonized_trucks if to_json else self.trucks

        except Exception as e:
            logging.error(e.message)
            res_dict = {'status': e.message}

        return res_dict
