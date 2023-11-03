from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from Conexion import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/transactions/',response_model=List[schemas.Transac])
def show_transac(db:Session=Depends(get_db)):
    transac = db.query(models.Transac).all()
    return transac

@app.post('/transacPOST/',response_model=schemas.Transac)
def create_transac(entrada:schemas.Transac,db:Session=Depends(get_db)):
    transactions = models.Transac(cantidadvendida = entrada.cantven,preciogalon=entrada.preciogal,cliente=entrada.cli,empleado=entrada.empl)
    db.add(transactions)
    db.commit()
    db.refresh(transactions)
    return transactions

@app.put('/transacPUT/{id}',response_model=schemas.Transac)
def update_transac(id:int,entrada:schemas.transacUpdate,db:Session=Depends(get_db)):
    transac = db.query(models.Transac).filter_by(id=id).first()
    transac.nombre=entrada.nombre
    db.commit()
    db.refresh(transac)
    return transac

@app.delete('/transacDEL/{id}',response_model=schemas.Respuesta)
def delete_transac(id:int,db:Session=Depends(get_db)):
    transac = db.query(models.Transac).filter_by(id=id).first()
    db.delete(transac)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta