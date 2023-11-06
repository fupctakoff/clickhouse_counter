from fastapi import APIRouter

app = APIRouter()


@app.get("/getWords", status_code=200)
async def response():
    return {"success": True}