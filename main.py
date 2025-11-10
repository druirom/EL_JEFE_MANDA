from typing import Dict, List, Tuple
from fastapi import FastAPI
from pydantic import BaseModel
import bisect

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    categories: List[Tuple[str,float]] #Lista que contiene las categorias a las cuales pertenece el producto y su ponderación

class Cliente(BaseModel):
    id : int
    user : str
    categories : Dict[str,int]
    boughtProducts : Dict[int, Product]
    preferences : List[str]
    restrictions : List[str]
    allProducts : List[Product]

    def recomendar (self, num:int):
        recomended = []
        for product in self.allProducts




