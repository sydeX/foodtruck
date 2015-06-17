import mock
from unittest import TestCase
from models.food_truck import FoodTruck

__author__ = 'sydex'

class TestFoodTruck(TestCase):
    def test_init_emptyArg(self):
        # Empty attributes argument
        self.assertTrue(FoodTruck(None))

    def test_init_listArg(self):
        attr = ['dummy1', 'dummy2']
        self.assertRaises( AttributeError, FoodTruck, attr)

    def test_init_dictionaryWithValidAttr(self):
        attr = {'applicant':'truck1'}
        ft = FoodTruck(attr)
        self.assertEqual(ft.applicant,'truck1')

    def test_init_dictionaryWithInvalidAttr(self):
        attr = {'dummy': '123'}
        ft = FoodTruck(attr)
        self.assertIsNone(ft.applicant)

    def test_hasLocationTrue(self):
        ft = FoodTruck()

        ft.latitude = 22
        ft.longitude = 33
        self.assertTrue(ft.hasLocation())

    def test_hasLocationFalse(self):
        ft = FoodTruck()

        ft.latitude =  None
        ft.longitude = 33
        self.assertFalse(ft.hasLocation())

        ft.latitude = None
        ft.longitude = None
        self.assertFalse(ft.hasLocation())

        ft.latitude = ''
        ft.longitude = 33
        self.assertFalse(ft.hasLocation())

    def test_updateDistance_noLocation(self):
        ft = FoodTruck()
        ft.updateDistance(1, 2)
        self.assertIsNone(ft.distance)


    def test_updateDistance_stringInput(self, hav):
        ft = FoodTruck()
        ft.latitude = 22
        ft.longitude = 33
        self.assertRaises(ValueError, ft.updateDistance, '55d', 2)

    @mock.patch('models.food_truck.haversine', return_value=5.22)
    def test_updateDistance_floatInput(self, haversine):
        ft = FoodTruck()
        ft.latitude = 22
        ft.longitude = 33
        ft.updateDistance('222.333', 222.333)
        self.assertEqual(ft.distance, 5.22)

