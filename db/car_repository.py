# The repository abstracts the database operations and provides an interface for data retrieval and storage.
from typing import List, Optional
from domain.model.car import Car


class CarRepository:

    def get_all_cars(self) -> List[Car] :
    # Result : list of cars
        list = []
        for i in range(20):
            id = i+1
            car = Car(id=id, name="Car"+str(id), price=id*1000.0,  brand="Peugeot", year=2020, color="Red")
            list.append(car)
        return list
    
    
    def get_cars(self, min_price: Optional[float]=None, max_price: Optional[float]=None) -> List[Car]:
    # Result : list of cars
        list = []
        for car in self.get_all_cars():
            # filtering with price
            if car_matches_filter_by_price(car, min_price, max_price):
                list.append(car)
        return list

    def get_car_by_id(self, id: int) -> Car:
    # Result : a single car or None if not found
        if (id < 1) or (id > 50):
            return None
        else:
            return Car(id=id, name="Car"+str(id), price=id*1000.0,  brand="Peugeot", year=2020, color="Red")

    def insert_car(self, car):
        raise NotImplementedError

    def update_car(self, car):
        raise NotImplementedError

    def delete_car(self, car_id: int):
        raise NotImplementedError    

#------------------------------------------------------------------------------------
# Filtering functions
#------------------------------------------------------------------------------------
def car_matches_filter_by_price(car: Car, min_price: Optional[float]=None, max_price: Optional[float]=None) -> bool:
    if min_price is not None:
        if car.price < min_price:
            return False
    if max_price is not None:
        if car.price > max_price:
            return False
    return True
def filter_cars_by_price(cars: List[Car], min_price: Optional[float]=None, max_price: Optional[float]=None) -> List[Car]:
# Result : list of cars
    list = []
    for car in cars:
        if car_matches_filter_by_price(car, min_price, max_price):
            list.append(car)
    return list
