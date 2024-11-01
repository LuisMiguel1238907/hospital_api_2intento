from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
import models
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PacienteCrear(BaseModel):
    nombre: str
    edad: int
    genero: str
    fecha_ingreso: str


class DoctorCrear(BaseModel):
    nombre: str
    especialidad: str
    telefono: str
    


class CitaCrear(BaseModel):
    fecha: datetime
    paciente_id: int
    doctor_id: int


@app.post("/pacientes/")
def crear_paciente(paciente: PacienteCrear, db: Session = Depends(get_db)):
    db_paciente = models.Paciente(nombre=paciente.nombre, edad=paciente.edad, genero=paciente.genero, fehca_ingreso = paciente.fecha_ingreso)
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente


@app.get("/pacientes/")
def leer_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pacientes = db.query(models.Paciente).offset(skip).limit(limit).all()
    return pacientes


@app.post("/doctores/")
def crear_doctor(doctor: DoctorCrear, db: Session = Depends(get_db)):
    db_doctor = models.Doctor(nombre=doctor.nombre, especialidad=doctor.especialidad, telefono=doctor.telefono)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


@app.get("/doctores/")
def leer_doctores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    doctores = db.query(models.Doctor).offset(skip).limit(limit).all()
    return doctores


@app.post("/citas/")
def crear_cita(cita: CitaCrear, db: Session = Depends(get_db)):
    db_cita = models.Cita(fecha=cita.fecha, paciente_id=cita.paciente_id, doctor_id=cita.doctor_id)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita


@app.get("/citas/")
def leer_citas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    citas = db.query(models.Cita).offset(skip).limit(limit).all()
    return citas
