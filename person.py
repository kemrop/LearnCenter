from  car import car


class person:
    def __init__(self, fname=None, lname=None, age=None, gender=None, address=None, city=None, zipcode=None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.name = self.fname + ' ' + self.lname
        self.car = None
        self.car = car("", "", "", None , None)

    def get_status_quo(self):
        car_make = self.car.get_car_make()
        if car_make == "Mercedez":
            return 'Cool'
        else:
            return 'Not Cool'


    def speculate_persons_age(self):
        """
        :rtype : object
        """
        car_mileage = self.car.get_car_mileage()
        car_year = int(self.car.get_car_year())

        if car_mileage <= 15001 and car_year >= 200:
            return True
        else:
            return False

    def get_full_name(self):
        """
        #:return:
        """
        if self.car.get_car_model() == "Camry" and self.car.get_car_mileage() > 2000:
            return self.fname + " " + self.lname
        else:
            return ""
