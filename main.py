import logging
from fastapi import FastAPI, Request

from rest.routes.item_router import router as item_router 
from rest.routes.car_router  import router as car_router 

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

description = """
My first FastAPI project. This is a simple project to demonstrate the use of FastAPI.
"""
logger.info("Starting application")

app = FastAPI(
    title = "My REST API",
    description = description,
    version = "0.0.1"
)

app.include_router(item_router, prefix="/items", tags=["items"])
app.include_router(car_router, prefix="/cars", tags=["cars"])

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/headers/")
async def get_all_headers(request: Request):
    headers = request.headers  # This returns a 'Headers' object
    accept = headers.get("accept")
    return {"headers": dict(headers), "accept": accept}  # Convert to a dictionary for JSON serialization