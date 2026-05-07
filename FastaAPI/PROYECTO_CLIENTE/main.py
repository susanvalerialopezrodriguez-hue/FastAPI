from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return{"mensaje": "hola mundo"}

lista_clientes = []
class cliente(BaseModel):
    id:int
    nombre: str
    edad: int
    descripcion: str | None = None

#Aplicacion de clientes

@app.get("/clientes")
def lista_clientes():
    return {"clientes": lista_clientes}

@app.get("/clientes",)
def crear_clientes(datos_cliente: cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "cliente creado"}

#RETO: Crear un nuevo endpoint y que me retorne un solo cliente 

@app.get("/clientes/{id}")
def get_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return {"cliente": cliente}
        return {"mensaje": "cliente no encontrado"}



