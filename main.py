from typing import Any, Dict, List, Set
from fastapi import FastAPI
from pydantic import BaseModel
import bisect

app = FastAPI()

class Product():
    id: int
    name: str
    categories: List[List[Any]] #Lista que contiene las categorias a las cuales pertenece el producto y su ponderación
    #imagen
    #precio: float

    def __init__(self, id, name, categories):
        self.id = id
        self.name = name
        self.categories = categories

class Client():
    id : int
    user : str
    categories : Dict[str,int]
    boughtProducts : Set[Product]
    preferences : List[str]
    restrictions : List[str]
    allProducts : Set[Product]

    def __init__(self,id,user,categories, bP, pref, rest, all):
        self.id = id
        self.user = user
        self.categories = categories
        self.boughtProducts = bP
        self.preferences = pref
        self.restrictions = rest
        self.allProducts = all

    def ponderate(self, product: Product) -> float:
        score = 0.0
        for category, weight in product.categories:
            if category in self.restrictions:
                return -1.0
            if category in self.preferences:
                score += (weight + 10) * 2
            elif category in self.categories:
                score += weight * self.categories[category]
        return score

    def recommend (self, num:int):
        recommended = SortedListProducts(num)
        for product in self.allProducts - self.boughtProducts:
            value = self.ponderate(product)
            recommended.insert(product,value)
        return recommended.getList()
        

class SortedListProducts():
    products: List[List]

    def __init__(self, l):
        self.products = [None] * l

    def insert (self, p:Product, value : float):
        for i in range(len(self.products)):
            if self.products[i] == None:
                self.products[i] = [p,value]
                break
            elif value > self.products[i][1]:
                if self.products[len(self.products)] != None:
                    self.products[i] = [p, value]
                    break
                else:
                    self.products.insert[i,[p,value]]
                    self.products.remove(None)
                    break
    def getList(self):
        l = []
        for i in self.products:
            if i == None:
                break
            else: 
                l.append[i[2]]
        return l

#SIMULATED DATA

all_products = [Product(0,"cereales_choco",[["Cereales", 0.8],["Chocolate", 0.4]]), Product(1,"chuleta_cerdo",[["Cerdo", 1],["Charcuteria", 0.2]])]
client = Client(1,"User1", {"Cerdo": 7}, {Product(1,"chuleta_cerdo",[["Cerdo", 1],["Charcuteria", 0.2]])}, ["Charcuteria"], ["Sin-Gluten"],all_products)

#ENDPOINTS

@app.get("/allProducts")
def get_all_products():
    return all_products

@app.get("/recommendedProducts")
def get_recommended_products():
    return client.recommend(5)

@app.get("/id")
def get_id():
    return client.id

@app.get("/user")
def get_user():
    return client.user
