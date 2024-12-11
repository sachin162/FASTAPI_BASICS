print("This is a main FIle which runs the server of Fast API")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory "database"
database = {}

# Define the schema for the items
class Item(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

# POST endpoint: Add a new item
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    print("This is a Post Call ")
    if item_id in database:
        raise HTTPException(status_code=400, detail="Item already exists")
    database[item_id] = item
    return {"item_id": item_id, "item": item}

# GET endpoint: Retrieve an item by ID
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = database.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": item}

# PUT endpoint: Update an existing item
@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    database[item_id] = updated_item
    return {"item_id": item_id, "updated_item": updated_item}

# Optional: GET all items
@app.get("/items")
async def read_all_items():
    return database

