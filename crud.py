from sqlalchemy.orm import Session

from . import models, schemas

def get_empleado(db: Session, empleado_id: int):
    return db.query(models.empleados).filter(models.empleados.id_empleado == empleado_id).first()

def get_empleado_by_nombre(db: Session, nombre: str):
    return db.query(models.empleados).filter(models.empleados.nombre == nombre).first()

def get_empleados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.empleados).offset(skip).limit(limit).all()

def create_empleado(db: Session, empleado: schemas.empleados):
    db_empleado = models.empleados(nombre=empleado.nombre, rol=empleado.rol)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def get_producto(db: Session, producto_id: int):
    return db.query(models.productos).filter(models.productos.id_producto == producto_id).first()

def get_producto_by_nombre(db: Session, nombre: str):
    return db.query(models.productos).filter(models.productos.nombre == nombre).first()

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.productos).offset(skip).limit(limit).all()

def create_producto(db: Session, producto: schemas.productos):
    db_producto = models.productos(nombre=producto.nombre, categoria=producto.categoria, descripcion=producto.descripcion)
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def get_precio(db: Session, precio_id: int):
    return db.query(models.precios).filter(models.precios.id_precio == precio_id).first()

def get_precio_by_id_tienda(db: Session, id_tienda: int):
    return db.query(models.precios).filter(models.precios.id_tienda == id_tienda).first()

def get_precio_by_id_producto(db: Session, id_producto: int):
    return db.query(models.precios).filter(models.precios.id_producto == id_producto).first()

def get_precios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.precios).offset(skip).limit(limit).all()

def create_precio(db: Session, precio: schemas.precios):
    db_precio = models.precios(id_tienda=precio.id_tienda, id_producto=precio.id_producto, precio=precio.precio)
    db.add(db_precio)
    db.commit()
    db.refresh(db_precio)
    return db_precio

