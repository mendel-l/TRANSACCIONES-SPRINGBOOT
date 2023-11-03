from typing import Optional
from pydantic import BaseModel

class Transac(BaseModel):
    id:Optional[int]
    cantidadvendida:str
    preciogalon:str
    cliente:str
    empleado:str

    class Config:
        orm_mode =True

class TransacUpdate(BaseModel):   
    nombre:str
   
    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str
   

