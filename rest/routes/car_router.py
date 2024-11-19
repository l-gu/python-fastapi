import logging
from typing import List, Optional
from fastapi import APIRouter, Request, Response, Header, Query

from rest.dto.car_dto import Car

logger = logging.getLogger(__name__)

# API router for the 'car' resource
router = APIRouter()

@router.get("/",
        # summary: A short description of the route (displayed as the route's name in Swagger UI).
        summary="Get all cars", 
        # description: A detailed explanation, which supports Markdown formatting.
        description="Returns a collection of cars",
        # tags: Organizes the routes in Swagger UI under specific headings. Useful for grouping routes logically 
        tags=["cars"],
        responses={200: {"description": "OK."},})
async def get_all(request: Request) -> List[Car]:
    logger.info("Get all cars")
    user_agent = request.headers.get("user-agent") # get the 'user-agent' header

    # Query parameters for filtering the cars
    min_price: float = Query(None, title="Minimum Price", description="Filter with a price greater than or equal to this value", example=10.0),
    max_price: float = Query(None, title="Maximum Price", description="Filter with a price less than or equal to this value", example=100.0),

    # Result : list of cars
    list = []
    for i in range(20):
        id = i+1
        car = Car(id=id, name="Car"+str(id), price=id*1000.0)
        list.append(car)

    # return [{"car_id": 1}, {"car_id": 2}]
    return list


@router.get("/{id}", 
        summary="Get a car for the given id",
        description="Returns a car or status 404 if the car is not found",
        tags=["cars"],
        responses={
            200: {"description": "OK."},
            404: {"description": "Not found."}, })
async def get_by_id(request: Request, id: int) -> Car:
    logger.info("Get car by id: %d", id)
    # Get car by id
    if id > 100:
        # If car is not found, return 404 status
        return Response(status_code=404)
    else:
        # If car is found, return the car   
        return Car(id=id, name="Car"+str(id), price=10000.0)
