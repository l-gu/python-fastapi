# The domain service contains business logic related to retrieving cars. 
# It uses the repository to fetch the data.
from typing import List, Optional
from domain.model.car import Car
from db.car_repository import CarRepository

class CarService:
    # Dependency injection to provide the CarRepository to the CarService
    def __init__(self, car_repository: CarRepository):
        self.car_repository = car_repository

    def get_all_cars(self) -> List[Car]:
        # Add any business logic here if necessary
        cars = self.car_repository.get_all_cars()
        return cars
    
    def get_cars(self, min_price: Optional[float]=None, max_price: Optional[float]=None) -> List[Car]:
        # Add any business logic here if necessary
        cars = self.car_repository.get_cars(min_price, max_price)
        return cars 

    def get_car_by_id(self, id: int) -> Car:
        # Add any business logic here if necessary
        return self.car_repository.get_car_by_id(id)

# Singleton for repository
car_repository = CarRepository()

# Singleton for domain service
car_service = CarService(car_repository)

# Provider function to provide the CarService for Dependency Injection
def get_car_service() -> CarService:
    # # db_session = SessionLocal()
    # # car_repository = CarRepository(db_session)
    # car_repository = CarRepository()
    #return CarService(car_repository)
    return car_service