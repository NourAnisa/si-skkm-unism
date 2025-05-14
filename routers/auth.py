
from fastapi import APIRouter
router = APIRouter(prefix="/auth")

@router.get("/login")
def login_page():
    return {"status": "login page ready"}
