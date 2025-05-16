# routers/prestasi.py

from fastapi import APIRouter, Form, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import PrestasiSKKM
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uuid

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post("/submit", response_class=HTMLResponse)
async def submit_data(
    request: Request,
    nama: str = Form(...),
    nim: str = Form(...),
    tahun_ajaran: str = Form(...),
    semester: str = Form(...),
    kegiatan: str = Form(...),
    penyelenggara: str = Form(...),
    tingkat: str = Form(...),
    capaian: str = Form(...),
    poin: int = Form(...),
    file_path: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    new_data = PrestasiSKKM(
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
        link_sertifikat=file_path,
    )
    db.add(new_data)
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
        "file_path": file_path
    })
