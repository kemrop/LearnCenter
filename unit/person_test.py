
import unittest
from mock import patch
from person import person


class TestCar(unittest.TestCase):
    def setUp(self):
        self.fname="Car"
        self.lname="Owner"
        self.age=30
        self.gender="Male"
        self.address='16600 LaughAlot St #306'
        self.city='Sioux Falls'
        self.zipcode='57104'
        unittest.TestCase.setUp(self)
        self.person=person(self.fname, self.lname, self.age, self.gender, self.address, self.city, self.zipcode)


    @patch('car.car.get_car_make')
    def test_shout_cool_for_car_model_of_person(self, mock_car):
        mock_car.return_value='Mercedez'
        actual = self.person.get_status_quo()
        expected = "Cool"
        self.assertEqual(expected, actual)




