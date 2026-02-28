from solution.service_layer import Product, ProductsService
from fastapi import FastAPI, HTTPException, status
from typing import List



app = FastAPI()


service = ProductsService()

@app.get("/products", response_model=List[Product])
def get_all_products() -> List[Product]:
    return service.get_all_products()

@app.get("/products/{product_id}", response_model=List[Product])
def get_product(product_id: int) -> Product:
    product = service.get_product_by_id(product_id)

    if product is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail ="Product not found",
        )
    
    return product



@app.post("/products",status_code = status.HTTP_201_CREATED, response_model= Product)
def create_product(name: str, description: str, price: float, stock: int) -> Product:
    return service.create_product(name= name, description= description, price= price, stock= stock)
