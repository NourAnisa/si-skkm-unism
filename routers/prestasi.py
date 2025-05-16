# routers/prestasi.py

from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import PrestasiSKKM
from utils import hitung_poin_skkm
import uuid

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/input", response_class=HTMLResponse)
async def tampilkan_form(request: Request):
    return templates.TemplateResponse("input_prestasi.html", {"request": request})

@router.post("/submit")
async def simpan_data(
    request: Request,
    nama: str = Form(...),
    nim: str = Form(...),
    tahun_ajaran: str = Form(...),
    semester: str = Form(...),
    kegiatan: str = Form(...),
    penyelenggara: str = Form(...),
    tingkat: str = Form(...),
    capaian: str = Form(...),
    link_sertifikat: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # Hitung poin SKKM otomatis
    poin = hitung_poin_skkm(tingkat, capaian)

    data = PrestasiSKKM(
        id=uuid.uuid4(),
        nama=nama,
        nim=nim,
        tahun_ajaran=tahun_ajaran,
        semester=semester,
        kegiatan=kegiatan,
        penyelenggara=penyelenggara,
        tingkat=tingkat,
        capaian=capaian,
        poin_skkm=poin,
        link_sertifikat=link_sertifikat
    )
    db.add(data)
    await db.commit()
    return templates.TemplateResponse("success.html", {
        "request": request,
        "nama": nama,
        "nim": nim,
        "ta": tahun_ajaran,
        "semester": semester,
        "kegiatan": kegiatan,
        "penyelenggara": penyelenggara,
        "tingkat": tingkat,
        "capaian": capaian,
        "poin": poin,
        "file_path": link_sertifikat
    })
