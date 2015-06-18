import mock
from unittest import TestCase
from models.food_truck_collection import FoodTruckCollection

class TestFoodTruckCollection(TestCase):
    @mock.patch('models.food_truck_collection.getCoordByAddress', return_value={"lat":1,"lng":2})
    @mock.patch('models.food_truck.FoodTruck')
    @mock.patch('models.food_truck.FoodTruck.toDict', return_value="dummyTruck")
    def test_getTruckData_whenAddressIsValid_thenReturnOkResult(self, toDict, FoodTruck, getCoordByAddress):
        ftc = FoodTruckCollection([FoodTruck(), FoodTruck()])
        res = ftc.getTruckData("dummyAddr")

        self.assertTrue(isinstance(res, dict))
        self.assertEqual(res['status'], 'OK')
        self.assertEqual(res['mapcenter'], getCoordByAddress.return_value)
        self.assertEqual(len(res['trucks']),2)

    @mock.patch('models.food_truck_collection.getCoordByAddress', return_value={"lat":1})
    @mock.patch('models.food_truck.FoodTruck')
    @mock.patch('models.food_truck.FoodTruck.toDict', return_value="dummyTruck")
    def test_getTruckData_whenAddressIsInvalid_thenReturnErrorResult(self, toDict, FoodTruck, getCoordByAddress):
        ftc = FoodTruckCollection([FoodTruck(), FoodTruck()])
        res = ftc.getTruckData("dummyAddr")

        self.assertNotEqual(res['status'], 'OK')