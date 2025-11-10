from typing import Dict, List, Tuple
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    categorias: List[Tuple[str,float]]

class Cliente(BaseModel):
    id : int
    user : str
    categoriasCli : Dict[str,int]
    comprados : Dict[int, Producto]
    preferencias : List[str]
    restricciones : List[str]
