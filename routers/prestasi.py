
from fastapi import APIRouter
router = APIRouter(prefix="/prestasi")

@router.get("/")
def get_data():
    return {"status": "prestasi data ready"}
