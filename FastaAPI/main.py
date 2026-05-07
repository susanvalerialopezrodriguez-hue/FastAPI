from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def inicio ():
    return {"mensaje": "Aprendiendo fastapi" }

@app.get("/saludo/{nombre}")
def saludo(nombre):
    return {"mensaje": f"Mi nombre es: {nombre}"}

#Crear otro endpoint, que me muestre la hora actual del servidor, debe importar el modulo datetime.

@app.get("/hora")
def hora_actual():
    ahora = datetime.now()
    return {
        "hora_actual": ahora.strftime("%H:%M:%S"),
        "fecha": ahora.strftime("%d/%m/%Y")
    }

