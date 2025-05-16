from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routers import prestasi, landing

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/data", StaticFiles(directory="data"), name="data")  # for Chart.js data

# Register routers
app.include_router(prestasi.router, prefix="/prestasi")
app.include_router(landing.router)

# Optional root fallback (bisa dihapus jika landing punya route "/")
@app.get("/")
def home():
    return {"message": "Form Prestasi SKKM siap"}
