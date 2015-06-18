import mock
from unittest import TestCase
from models.food_truck import FoodTruck

class TestFoodTruck(TestCase):

    def test_whenLatitudeAndLongitudeIsSet_thenHasLocationIsTrue(self):
        foodTruck = self.createFoodTruck(latitude=22, longitude=23)
        self.assertTrue(foodTruck.hasLocation())

    def test_whenLatitudeOrLongitudeIsNotSet_thenHasLocationFalse(self):
        foodTruck = self.createFoodTruck()
        self.assertFalse(foodTruck.hasLocation())

        foodTruck = self.createFoodTruck(latitude=None, longitude=33)
        self.assertFalse(foodTruck.hasLocation())

        foodTruck = self.createFoodTruck(latitude='', longitude=33)
        self.assertFalse(foodTruck.hasLocation())

    def test_whenFoodTruckHasNoLocation_thenDistanceFromCoordsIsNone(self):
        foodTruck = self.createFoodTruck()
        foodTruck.computeDistanceFromCoords(1, 2)
        self.assertIsNone(foodTruck.distance)

    @mock.patch('models.food_truck.haversine', return_value=5.22)
    def test_whenFoodTruckHasLocation_thenDistanceFromCoordsIsCorrect(self, haversine):
        foodTruck = self.createFoodTruck(latitude=22, longitude=23)
        foodTruck.computeDistanceFromCoords(222.333, 222.333)
        self.assertEqual(foodTruck.distance, 5.22)

    def createFoodTruck(self, latitude=None, longitude=None):
        return FoodTruck("name", "foodItems", "address", latitude, longitude)
