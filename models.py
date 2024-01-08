from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class empleados(Base):
    __tablename__ = "empleados"
    
    id_empleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    rol = Column(String, index=True)

class productos(Base):
    __tablename__ = "productos"
    
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    categoria = Column(Integer, index=True)
    descripcion = Column(String, index=True)

class precios(Base):
    __tablename__ = "precios"
    
    id_precio = Column(Integer, primary_key=True, index=True)
    id_tienda = Column(Integer, index=True)
    id_producto = Column(Integer, index=True)
    precio = Column(Integer, index=True)

