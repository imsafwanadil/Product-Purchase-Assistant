from fastapi import FastAPI
from app.api import chat, products

app = FastAPI(title="Purchase Decision Assistant")

app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
def root():
    return {"message": "Purchase Decision Assistant backend running"}
