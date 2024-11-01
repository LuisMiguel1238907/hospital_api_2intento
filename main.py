from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy import func
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
    db_paciente = models.Paciente(nombre=paciente.nombre, edad=paciente.edad, genero=paciente.genero)
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente


@app.get("/pacientes/")
def leer_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pacientes = db.query(models.Paciente).offset(skip).limit(limit).all()
    return pacientes

@app.get("/pacientes/edad/max/")
def edad_maxima(db: Session = Depends(get_db)):
    max_edad = db.query(func.max(models.Paciente.edad)).scalar()
    return {"edad_maxima": max_edad}


@app.get("/pacientes/edad/min/")
def edad_minima(db: Session = Depends(get_db)):
    min_edad = db.query(func.min(models.Paciente.edad)).scalar()
    return {"edad_minima": min_edad}

@app.get("/pacientes/edad/promedio/")
def edad_promedio(db: Session = Depends(get_db)):
    avg_edad = db.query(func.avg(models.Paciente.edad)).scalar()
    return {"edad_promedio": avg_edad}


@app.get("/pacientes/genero/")
def contar_genero(db: Session = Depends(get_db)):
    conteo_genero = db.query(models.Paciente.genero, func.count(models.Paciente.id)).group_by(models.Paciente.genero).all()
    return [{"genero": genero, "cantidad": cantidad} for genero, cantidad in conteo_genero]

@app.get("/pacientes/grupo_etario/")
def contar_grupo_etario(db: Session = Depends(get_db)):
    ninos = db.query(func.count(models.Paciente.id)).filter(models.Paciente.edad < 18).scalar()
    adultos = db.query(func.count(models.Paciente.id)).filter(models.Paciente.edad.between(18, 64)).scalar()
    tercera_edad = db.query(func.count(models.Paciente.id)).filter(models.Paciente.edad >= 65).scalar()
    return {
        "niños": ninos,
        "adultos": adultos,
        "tercera_edad": tercera_edad
    }


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

