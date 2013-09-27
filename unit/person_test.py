
import unittest
from mock import patch
from person import person


class TestCar(unittest.TestCase):
    def setUp(self):
        self.fname = "Car"
        self.lname = "Owner"
        self.age = 30
        self.gender = "Male"
        self.address = '16600 LaughAlot St #306'
        self.city = 'Sioux Falls'
        self.zipcode = '57104'
        unittest.TestCase.setUp(self)
        self.person=person(self.fname, self.lname, self.age, self.gender, self.address, self.city, self.zipcode)


    @patch('car.car.get_car_make')
    def test_shout_cool_for_car_model_of_person(self, mock_car):
        mock_car.return_value = 'Mercedez'
        actual = self.person.get_status_quo()
        expected = "Cool"
        self.assertEqual(expected, actual)

    @patch('car.car.get_car_make')
    def test_shout_cool_for_car_model_of_person(self, mock_car):
        mock_car.return_value = 'Mazda'
        actual = self.person.get_status_quo()
        expected = "Not Cool"
        self.assertEqual(expected, actual)

    @patch('car.car.get_car_mileage')
    @patch('car.car.get_car_year')
    def test_college_graduate(self, mock_car_mileage, mock_car_year):
        mock_car_mileage.return_value = 15001
        mock_car_year.return_value = 1
        actual = self.person.speculate_persons_age()
        self.assertTrue(actual)

    #Test when get Person full name only if he owns a Camry and the camry is over 15000 Mileage
    @patch('car.car.get_car_mileage')
    @patch('car.car.get_car_model')
    def test_get_full_name(self, mock_car_model, mock_car_mileage):
        mock_car_model.return_value = "Camry"
        mock_car_mileage.return_value = 15000

        expected = "Car Owner"
        actual = self.person.get_full_name()

        self.assertEqual(expected, actual)








