from  car import car


class person:
    def __init__(self,fname=None, lname=None, age=None, gender=None, address=None, city=None, zipcode=None):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
        self.address=address
        self.city=city
        self.zipcode=zipcode
        self.name = self.fname + ' ' + self.lname
        self.car = None
        self.car = car("Mercedez","Benze","2012", 15000, self.name)

    def get_status_quo(self):
        car_model = self.car.get_car_make()
        if car_model == "Mercedez":
            return 'Cool'
        else:
            return 'Not Cool'







