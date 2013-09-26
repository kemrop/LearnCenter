class car:
  def __init__(self, make=None, model=None, year=None, mileage=None, owner=None):
      self.make = make
      self.model=model
      self.year=year
      self.mileage=mileage
      self.owner=owner

  def get_car_make(self):
      return self.make

  def get_car_model(self):
      return self.model

  def get_car_year(self):
      return self.year

  def get_car_mileage(self):
      return self.mileage

  def get_car_owner(self):
      return self.owner