import logging
from typing import List, Optional
from fastapi import APIRouter, Request, Response, Header, Query, Depends
from domain.services.car_service import CarService, get_car_service
from domain.model.car import Car
# from dependency_injection import get_car_service
from rest.dto.car_dto import CarDto

logger = logging.getLogger(__name__)

# API router for the 'car' resource
router = APIRouter()

#------------------------------------------------------------------------------------
# GET ALL 
#------------------------------------------------------------------------------------
@router.get("",
        # summary: A short description of the route (displayed as the route's name in Swagger UI).
        summary="Get all cars", 
        # description: A detailed explanation, which supports Markdown formatting.
        description="Returns a collection of cars",
        # tags: Organizes the routes in Swagger UI under specific headings. Useful for grouping routes logically 
        tags=["cars"],
        responses={200: {"description": "OK."},})
async def get(
    # Service dependency injection
    car_service: CarService = Depends(get_car_service),
    # Path parameters
    # (none)
    # Header parameters ("...": required, "None": optional)
    brand: str = Header(None, description="Brand of the car (in header)", min_length=1, max_length=20, example="Peugeot"),
    # Query parameters for filtering the cars ("...": required, "None": optional)
    min_price: float = Query(None, title="Minimum Price", description="Filter with a price greater than or equal to this value", example=10.0),
    max_price: float = Query(None, title="Maximum Price", description="Filter with a price less than or equal to this value", example=100.0),
    ) -> List[CarDto]:

    # Query parameters for filtering the cars
    logger.info("GET cars. Query parameters: min_price=%s, max_price=%s", min_price, max_price)

    list = car_service.get_cars(min_price, max_price)
    # domain to dto conversion
    result = []
    for car in list:
        result.append(CarDto(id=car.id, name=car.name, price=car.price))
    return result

def filterOK(car: CarDto, min_price: Optional[float]=None, max_price: Optional[float]=None) -> bool:
    if min_price is not None:
        if car.price < min_price:
            return False
    if max_price is not None:
        if car.price > max_price:
            return False
    return True

#------------------------------------------------------------------------------------
# GET BY ID  
#------------------------------------------------------------------------------------
@router.get("/{id}", 
        summary="Get a car for the given id",
        description="Returns a car or status 404 if the car is not found",
        tags=["cars"],
        responses={
            200: {"description": "OK."},
            404: {"description": "Not found."}, })
async def get_by_id(
    # Path parameters
    id: int,
    # Service dependency injection
    car_service: CarService = Depends(get_car_service),
    # Header parameters ("...": required, "None": optional)
    brand: str = Header(None, description="Brand of the car (in header)", min_length=1, max_length=20, example="Peugeot"),
    ) -> CarDto:
    logger.info("Get car by id: %d", id)
    # Get car by id
    car = car_service.get_car_by_id(id)
    if (car is None):
        # If car is not found, return 404 status
        return Response(status_code=404)
    else:
        # If car is found, return the car payload
        return CarDto(id=car.id, name=car.name, price=car.price)
