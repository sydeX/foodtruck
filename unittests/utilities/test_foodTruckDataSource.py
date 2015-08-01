import mock
from unittest import TestCase
from utilities.food_truck_data_source import FoodTruckDataSource


class TestFoodTruckDataSource(TestCase):
    @mock.patch('utilities.food_truck_data_source.load_url', return_value=None)
    def test_whenReturnedDataIsNone_thenFoodTruckCollectionIsEmpty(self, load_url):
        food_truck_collection = FoodTruckDataSource.get_food_trucks()
        self.assertEqual(len(food_truck_collection), 0)

    @mock.patch('utilities.food_truck_data_source.load_url', return_value=[{"applicant": "dummy"}])
    def test_whenReturnedDataHasNoLocation_thenFoodTruckCollectionIsEmpty(self, load_url):
        food_truck_collection = FoodTruckDataSource.get_food_trucks()
        self.assertEqual(len(food_truck_collection), 0)

    @mock.patch('utilities.food_truck_data_source.load_url', return_value=[{"latitude": 2, "longitude": 3}])
    def test_whenReturnedDataHasLocation_thenFoodTruckCollectionIsNotEmpty(self, load_url):
        food_truck_collection = FoodTruckDataSource.get_food_trucks()
        self.assertEqual(len(food_truck_collection), 1)
