
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class PrestasiCreate(BaseModel):
    nama_kegiatan: str
    jenis: str
    tingkat: str
    peran: str
    tahun: str
    sertifikat: str
    poin: int
