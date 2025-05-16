from sqlalchemy import Column, String, Integer, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class PrestasiSKKM(Base):
    __tablename__ = "prestasi_skkm"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nama = Column(String)
    nim = Column(String)
    tahun_ajaran = Column(String)
    semester = Column(String)
    kegiatan = Column(Text)
    penyelenggara = Column(String)
    tingkat = Column(String)
    capaian = Column(String)
    poin_skkm = Column(Integer)
    link_sertifikat = Column(String)
    created_at = Column(TIMESTAMP, server_default="now()")
