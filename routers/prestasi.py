
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/input", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("input_prestasi.html", {"request": request})

@router.post("/submit", response_class=HTMLResponse)
async def submit_form(
    request: Request,
    nama: str = Form(...),
    nim: str = Form(...),
    ta: str = Form(...),
    semester: str = Form(...),
    kegiatan: str = Form(...),
    penyelenggara: str = Form(...),
    tingkat: str = Form(...),
    capaian: str = Form(...),
    link_sertifikat: str = Form(...)
):
    poin = hitung_poin(tingkat, capaian)

    return templates.TemplateResponse("success.html", {
        "request": request,
        "nama": nama,
        "nim": nim,
        "ta": ta,
        "semester": semester,
        "kegiatan": kegiatan,
        "penyelenggara": penyelenggara,
        "tingkat": tingkat,
        "capaian": capaian,
        "poin": poin,
        "file_path": link_sertifikat
    })

def hitung_poin(tingkat: str, capaian: str) -> int:
    map_poin = {
        "Juara I": {"Lokal": 23, "Nasional": 50, "Internasional": 65},
        "Juara II": {"Lokal": 18, "Nasional": 40, "Internasional": 55},
        "Juara III": {"Lokal": 13, "Nasional": 30, "Internasional": 45},
        "Peserta": {"Lokal": 5, "Nasional": 10, "Internasional": 25}
    }
    return map_poin.get(capaian, {}).get(tingkat, 0)
