from fastapi import FastAPI, HTTPException

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