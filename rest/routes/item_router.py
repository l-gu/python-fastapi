from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all():
    return [{"item_id": 1}, {"item_id": 2}]

@router.get("/{id}")
async def get_by_id(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
