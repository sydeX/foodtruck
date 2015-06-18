import mock
from unittest import TestCase
from utilities.food_truck_data_source import FoodTruckDataSource

class TestFoodTruckDataSource(TestCase):
    @mock.patch('utilities.food_truck_data_source.loadURL', return_value=None)
    def test_whenReturnedDataIsNone_thenFoodTruckCollectionIsEmpty(self, loadURL):
        foodTruckCollection = FoodTruckDataSource.getFoodTrucks()
        self.assertEqual(len(foodTruckCollection), 0)

    @mock.patch('utilities.food_truck_data_source.loadURL', return_value=[{"applicant":"dummy"}])
    def test_whenReturnedDataHasNoLocation_thenFoodTruckCollectionIsEmpty(self, loadURL):
        foodTruckCollection = FoodTruckDataSource.getFoodTrucks()
        self.assertEqual(len(foodTruckCollection), 0)

    @mock.patch('utilities.food_truck_data_source.loadURL', return_value=[{"latitude":2, "longitude":3}])
    def test_whenReturnedDataHasLocation_thenFoodTruckCollectionIsNotEmpty(self, loadURL):
        foodTruckCollection = FoodTruckDataSource.getFoodTrucks()
        self.assertEqual(len(foodTruckCollection), 1)