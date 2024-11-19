from typing import List, Optional
from fastapi import APIRouter, Request, Response, Header

from rest.dto.car_dto import Car

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
    user_agent = request.headers.get("user-agent") # get the 'user-agent' header

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
    # Get car by id
    if id > 100:
        # If car is not found, return 404 status
        return Response(status_code=404)
    else:
        # If car is found, return the car   
        return Car(id=id, name="Car"+str(id), price=10000.0)
