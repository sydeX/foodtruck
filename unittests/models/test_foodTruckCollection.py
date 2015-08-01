import mock
from unittest import TestCase
from models.food_truck_collection import FoodTruckCollection


class TestFoodTruckCollection(TestCase):
    @mock.patch('models.food_truck_collection.get_coord_by_address', return_value={"lat": 1, "lng": 2})
    @mock.patch('models.food_truck.FoodTruck')
    @mock.patch('models.food_truck.FoodTruck.to_dict', return_value="dummy_truck")
    def test_getTruckData_whenAddressIsValid_thenReturnOkResult(self, to_dict, foodtruck, get_coord_by_address):
        ftc = FoodTruckCollection([foodtruck(), foodtruck()])
        res = ftc.get_truck_data("dummy_addr")

        self.assertTrue(isinstance(res, dict))
        self.assertEqual(res['status'], 'OK')
        self.assertEqual(res['mapcenter'], get_coord_by_address.return_value)
        self.assertEqual(len(res['trucks']), 2)

    @mock.patch('models.food_truck_collection.get_coord_by_address', return_value={"lat": 1})
    @mock.patch('models.food_truck.FoodTruck')
    @mock.patch('models.food_truck.FoodTruck.to_dict', return_value="dummy_truck")
    def test_getTruckData_whenAddressIsInvalid_thenReturnErrorResult(self, to_dict, foodtruck, get_coord_by_address):
        ftc = FoodTruckCollection([foodtruck(), foodtruck()])
        res = ftc.get_truck_data("dummy_addr")

        self.assertNotEqual(res['status'], 'OK')
