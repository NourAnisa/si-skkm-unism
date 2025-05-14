from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, prestasi

app = FastAPI()
@app.get("/")
def home():


templates = Jinja2Templates(directory="templates")
app.include_router(auth.router)
app.include_router(prestasi.router)
    return {"message": "SKKM UNISM is running with full features ✅"} import os
from fastapi.staticfiles import StaticFiles

if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
