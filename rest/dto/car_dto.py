from uuid import UUID
from pydantic import BaseModel, Field

class CarDto(BaseModel):
    id: int = Field(..., title="id", description="The unique identifier for the car")  # '...' => Required
    name: str = Field(..., title="name", description="The name of the car")  # Required
    price: float = Field(default=None, title="price", description="The price of the car") 

