import mock
from unittest import TestCase
from models.food_truck import FoodTruck


class TestFoodTruck(TestCase):

    def test_whenLatitudeAndLongitudeIsSet_thenHasLocationIsTrue(self):
        food_truck = self.createFoodTruck(latitude=22, longitude=23)
        self.assertTrue(food_truck.has_location())

    def test_whenLatitudeOrLongitudeIsNotSet_thenHasLocationFalse(self):
        food_truck = self.createFoodTruck()
        self.assertFalse(food_truck.has_location())

        food_truck = self.createFoodTruck(latitude=None, longitude=33)
        self.assertFalse(food_truck.has_location())

        food_truck = self.createFoodTruck(latitude='', longitude=33)
        self.assertFalse(food_truck.has_location())

    def test_whenFoodTruckHasNoLocation_thenDistanceFromCoordsIsNone(self):
        food_truck = self.createFoodTruck()
        food_truck.compute_distance_from_coords(1, 2)
        self.assertIsNone(food_truck.distance)

    @mock.patch('models.food_truck.haversine', return_value=5.22)
    def test_whenFoodTruckHasLocation_thenDistanceFromCoordsIsCorrect(self, haversine):
        food_truck = self.createFoodTruck(latitude=22, longitude=23)
        food_truck.compute_distance_from_coords(222.333, 222.333)
        self.assertEqual(food_truck.distance, 5.22)

    def createFoodTruck(self, latitude=None, longitude=None):
        return FoodTruck("name", "foodItems", "address", latitude, longitude)
