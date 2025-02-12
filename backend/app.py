# Import Library
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import qa, chain  # Ensure chatbot.py exists with qa and chain

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Ecommerce Product Recommendation with ChatGPT"}

class Item(BaseModel):
    department: str
    category: str
    brand: str
    price: str

@app.post("/manual")
async def manual(item: Item):
    response = chain.run(
        department=item.department,
        category=item.category,
        brand=item.brand,
        price=item.price
    )
    return {"response": response}  # Fixed return type

class Query(BaseModel):
    query: str

@app.post("/chatbot")
async def get_answer(query: Query):
    response = qa.run(query=query.query)
    return {"response": response}  # Fixed return type

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
