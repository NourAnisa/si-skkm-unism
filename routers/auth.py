
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

users = {
    "mahasiswa01": {"password": "123", "role": "mahasiswa"},
    "dosen01": {"password": "456", "role": "dosen"},
    "admin01": {"password": "admin", "role": "admin"}
}

@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
    user = users.get(username)
    if user and user["password"] == password:
        role = user["role"]
        if role == "mahasiswa":
            return RedirectResponse(url="/auth/dashboard/mahasiswa", status_code=302)
        elif role == "dosen":
            return RedirectResponse(url="/auth/dashboard/dosen", status_code=302)
        elif role == "admin":
            return RedirectResponse(url="/auth/dashboard/admin", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Login gagal"})

@router.get("/dashboard/{role}", response_class=HTMLResponse)
def dashboard_role(request: Request, role: str):
    return templates.TemplateResponse("dashboard.html", {"request": request, "role": role})
