from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Modelo de Paciente
class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    edad = Column(Integer)
    genero = Column(String(10))
    diagnostico = Column(String(250))

# Modelo de Doctor
class Doctor(Base):
    __tablename__ = "doctores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    especialidad = Column(String(100))

# Modelo de Cita Médica
class Cita(Base):
    __tablename__ = "citas_medicas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    doctor_id = Column(Integer, ForeignKey("doctores.id"))

    paciente = relationship("Paciente")
    doctor = relationship("Doctor")
