from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok" }

@app.get("/item")
def get_item(id: int):
    if id > 9:
        raise HTTPException(status_code=500, detail="Internal server error")
    if id <= 0:
        raise HTTPException(status_code=400, detail="Invalid ID")
    
    return {
        "id": id,
        "name": "Test"
    }

@app.post("/item", status_code=201)
async def create_item(request: Request):
    body = await request.json()

    if "name" not in body or "price" not in body:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    name = body["name"]
    price = body["price"]

    if not isinstance(name, str) or not isinstance(price, (int, float)):
        raise HTTPException(status_code=400, detail="Invalid field types")

    
    if price <= 0:
        raise HTTPException(status_code=400, detail="Price must be positive")

    return {
        "id": 1,
        "name": name,
        "price": price
    }