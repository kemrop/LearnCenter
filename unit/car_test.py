import unittest
from car import car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car_make = "Toyota"
        self.car_model = "Camry"
        self.car_year = "1999"
        self.car_owner = "Car Owner"
        self.car_mileage = 140000
        unittest.TestCase.setUp(self)
        self.car = car(self.car_make, self.car_model, self.car_year, self.car_mileage, self.car_owner)

    def test_get_car_make(self):
        expected = "Toyota"
        actual = self.car.get_car_make()
        self.assertEqual(expected, actual)

    def test_get_car_model(self):
        expected = 'Camry'
        actual = self.car.get_car_model()
        self.assertEqual(expected, actual)

    def test_get_car_year(self):
        expected = '1999'
        actual = self.car.get_car_year()
        self.assertEqual(expected, actual)

    def test_get_car_mileage(self):
        expected = 140000
        actual = self.car.get_car_mileage()
        self.assertEqual(expected, actual)

    def test_get_car_owner(self):
        expected = 'Car Owner'
        actual = self.car.get_car_owner()
        self.assertEqual(expected, actual)
