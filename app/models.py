from sqlalchemy import Column, Integer, String, double
from Conexion import Base

class Transac(Base):
    __tablename__ = 'transactions'
    id = Column(Integer,primary_key=True,index=True)
    cantidadvendida = Column(double)
    preciogalon = Column(double)
    cliente = Column(String(100))
    empleado = Column(String(100))

