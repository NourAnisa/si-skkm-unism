
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

class Prestasi(Base):
    __tablename__ = "prestasi"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    nama_kegiatan = Column(String)
    jenis = Column(String)
    tingkat = Column(String)
    peran = Column(String)
    tahun = Column(String)
    poin = Column(Integer)
    sertifikat = Column(String)

    user = relationship("User", back_populates="prestasi")
User.prestasi = relationship("Prestasi", back_populates="user")
