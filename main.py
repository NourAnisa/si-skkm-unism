import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, prestasi

# Buat folder uploads jika belum ada
if not os.path.exists("uploads"):
    os.makedirs("uploads")

app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static dan uploads
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Templates dan routers
templates = Jinja2Templates(directory="templates")
app.include_router(auth.router)
app.include_router(prestasi.router)

# Root endpoint
@app.get("/")
def home():
    return {"message": "SKKM UNISM is running with full features ✅"}
