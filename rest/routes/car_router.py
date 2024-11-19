import logging
from typing import List, Optional
from fastapi import APIRouter, Request, Response, Header, Query

from rest.dto.car_dto import Car

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
async def get_all(
    # Path parameters
    # (none)
    # Header parameters ("...": required, "None": optional)
    brand: str = Header(None, description="Brand of the car (in header)", min_length=1, max_length=20, example="Peugeot"),
    # Query parameters for filtering the cars ("...": required, "None": optional)
    min_price: float = Query(None, title="Minimum Price", description="Filter with a price greater than or equal to this value", example=10.0),
    max_price: float = Query(None, title="Maximum Price", description="Filter with a price less than or equal to this value", example=100.0),
    ) -> List[Car]:

    logger.info("Get all cars")

    # Query parameters for filtering the cars
    logger.info("Query parameters: min_price=%s, max_price=%s", min_price, max_price)

    # Result : list of cars
    list = []
    for i in range(20):
        id = i+1
        car = Car(id=id, name="Car"+str(id), price=id*1000.0)
        # filtering with price
        if ( filterOK(car, min_price, max_price) ):
            list.append(car)

    return list

def filterOK(car: Car, min_price: Optional[float]=None, max_price: Optional[float]=None) -> bool:
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
    # Header parameters ("...": required, "None": optional)
    brand: str = Header(None, description="Brand of the car (in header)", min_length=1, max_length=20, example="Peugeot"),
    ) -> Car:
    logger.info("Get car by id: %d", id)
    # Get car by id
    if id > 100:
        # If car is not found, return 404 status
        return Response(status_code=404)
    else:
        # If car is found, return the car   
        return Car(id=id, name="Car"+str(id), price=10000.0)
