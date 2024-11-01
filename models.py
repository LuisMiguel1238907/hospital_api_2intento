from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, VARCHAR, Date
from sqlalchemy.orm import relationship
from database import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    edad = Column(Integer)
    genero = Column(String(10))
    


<<<<<<< HEAD
=======

>>>>>>> b1b442f031814a5a31b364057507db742fedb523
class Doctor(Base):
    __tablename__ = "doctores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    especialidad = Column(String(100))
    telefono = Column(VARCHAR(100))


<<<<<<< HEAD
=======

>>>>>>> b1b442f031814a5a31b364057507db742fedb523
class Cita(Base):
    __tablename__ = "citas_medicas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    doctor_id = Column(Integer, ForeignKey("doctores.id"))

    paciente = relationship("Paciente")
    doctor = relationship("Doctor")


class Citas(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True, index=True)
    id_paciente = Column(Integer, ForeignKey("pacientes.id"))
    id_doctor = Column(Integer, ForeignKey("doctores.id"))
    fecha_hora = Column(Date)
    motivo = Column(VARCHAR(100))
    


