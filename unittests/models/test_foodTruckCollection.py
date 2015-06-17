import mock
from unittest import TestCase
from models.food_truck_collection import FoodTruckCollection

__author__ = 'sydex'


class TestFoodTruckCollection(TestCase):

    @mock.patch('models.food_truck_collection.loadURL', return_value=None)
    def test_createfromURL_noneURL(self, loadURL):
        ftc = FoodTruckCollection.createfromURL('dummy')
        self.assertEqual(len(ftc), 0)

    @mock.patch('models.food_truck_collection.loadURL', return_value=[{"applicant":"dummpy"}])
    def test_createfromURL_dataURL_noLocation(self, loadURL):
        ftc = FoodTruckCollection.createfromURL('dummy')
        self.assertEqual(len(ftc), 0)

    @mock.patch('models.food_truck_collection.loadURL', return_value=[{"latitude":2, "longitude":3}])
    def test_createfromURL_dataURL_withLocation(self, loadURL):
        ftc = FoodTruckCollection.createfromURL('dummy')
        self.assertEqual(len(ftc), 1)

    @mock.patch('models.food_truck_collection.getCoordByAddress', return_value={"lat":1,"lng":2})
    @mock.patch('models.food_truck.FoodTruck')
    @mock.patch('models.food_truck_collection.FoodTruck.toDict', return_value="dummyTruck")
    def test_getTruckData_statusOK(self, toDict, FoodTruck, getCoordByAddress):
        ftc = FoodTruckCollection([FoodTruck(), FoodTruck()])
        res = ftc.getTruckData("dummyAddr")

        self.assertTrue(isinstance(res, dict))
        self.assertEqual(res['status'], 'OK')
        self.assertEqual(res['mapcenter'], getCoordByAddress.return_value)
        self.assertEqual(len(res['trucks']),2)

    @mock.patch('models.food_truck_collection.getCoordByAddress', return_value={"lat":1})
    @mock.patch('models.food_truck.FoodTruck')
    @mock.patch('models.food_truck_collection.FoodTruck.toDict', return_value="dummyTruck")
    def test_getTruckData_statusError(self, toDict, FoodTruck, getCoordByAddress):
        ftc = FoodTruckCollection([FoodTruck(), FoodTruck()])
        res = ftc.getTruckData("dummyAddr")

        self.assertNotEqual(res['status'], 'OK')