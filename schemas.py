from pydantic import BaseModel

class empleados(BaseModel):
    id_empleado: int
    nombre: str
    rol: str

class productos(BaseModel):
    id_producto: int
    nombre: str
    categoria: int
    descripcion: str

class precios(BaseModel):
    id_precio: int
    id_tienda: int
    id_producto: int
    precio: int

