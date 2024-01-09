from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/empleados/", response_model=schemas.empleados)
def create_empleado(empleado: schemas.empleados, db: Session = Depends(get_db)):
    db_empleado = crud.get_empleado_by_nombre(db, nombre=empleado.nombre)
    if db_empleado:
        raise HTTPException(status_code=400, detail="Nombre ya registrado")
    return crud.create_empleado(db=db, empleado=empleado)



@app.get("/empleados/{empleado_id}", response_model=schemas.empleados)
def read_empleado(empleado_id: int, db: Session = Depends(get_db)):
    db_empleado = crud.get_empleado(db, empleado_id=empleado_id)
    if db_empleado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_empleado

@app.post("/productos/", response_model=schemas.productos)
def create_producto(producto: schemas.productos, db: Session = Depends(get_db)):
    db_producto = crud.get_producto_by_nombre(db, nombre=producto.nombre)
    if db_producto:
        raise HTTPException(status_code=400, detail="Nombre ya registrado")
    return crud.create_producto(db=db, producto=producto)



@app.get("/productos/{producto_id}", response_model=schemas.productos)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.post("/precios/", response_model=schemas.precios)
def create_precio(precio: schemas.precios, db: Session = Depends(get_db)):
    db_precio = crud.get_precio_by_id_tienda(db, id_tienda=precio.id_tienda)
    if db_precio:
        raise HTTPException(status_code=400, detail="Precio ya registrado")
    return crud.create_precio(db=db, precio=precio)



@app.get("/precios/{precio_id}", response_model=schemas.precios)
def read_precio(precio_id: int, db: Session = Depends(get_db)):
    db_precio = crud.get_precio(db, precio_id=precio_id)
    if db_precio is None:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return db_precio

@app.get("/precios/tienda/{id_tienda}", response_model=schemas.precios)
def read_precio_by_id_tienda(id_tienda: int, db: Session = Depends(get_db)):
    db_precio = crud.get_precio_by_id_tienda(db, id_tienda=id_tienda)
    if db_precio is None:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return db_precio

@app.get("/precios/producto/{id_producto}", response_model=schemas.precios)
def read_precio_by_id_producto(id_producto: int, db: Session = Depends(get_db)):
    db_precio = crud.get_precio_by_id_producto(db, id_producto=id_producto)
    if db_precio is None:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    return db_precio

