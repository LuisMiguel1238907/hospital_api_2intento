from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
import models
from database import SessionLocal, engine

# Inicializar los modelos en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo Pydantic para crear un paciente
class PacienteCrear(BaseModel):
    nombre: str
    edad: int
    genero: str
    diagnostico: str

# Modelo Pydantic para crear un doctor
class DoctorCrear(BaseModel):
    nombre: str
    especialidad: str

# Modelo Pydantic para crear una cita
class CitaCrear(BaseModel):
    fecha: datetime
    paciente_id: int
    doctor_id: int

# Endpoint para crear un paciente
@app.post("/pacientes/")
def crear_paciente(paciente: PacienteCrear, db: Session = Depends(get_db)):
    db_paciente = models.Paciente(nombre=paciente.nombre, edad=paciente.edad, genero=paciente.genero, diagnostico=paciente.diagnostico)
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

# Endpoint para consultar todos los pacientes
@app.get("/pacientes/")
def leer_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pacientes = db.query(models.Paciente).offset(skip).limit(limit).all()
    return pacientes

# Endpoint para crear un doctor
@app.post("/doctores/")
def crear_doctor(doctor: DoctorCrear, db: Session = Depends(get_db)):
    db_doctor = models.Doctor(nombre=doctor.nombre, especialidad=doctor.especialidad)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

# Endpoint para consultar todos los doctores
@app.get("/doctores/")
def leer_doctores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    doctores = db.query(models.Doctor).offset(skip).limit(limit).all()
    return doctores

# Endpoint para crear una cita médica
@app.post("/citas/")
def crear_cita(cita: CitaCrear, db: Session = Depends(get_db)):
    db_cita = models.Cita(fecha=cita.fecha, paciente_id=cita.paciente_id, doctor_id=cita.doctor_id)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

# Endpoint para consultar todas las citas médicas
@app.get("/citas/")
def leer_citas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    citas = db.query(models.Cita).offset(skip).limit(limit).all()
    return citas
