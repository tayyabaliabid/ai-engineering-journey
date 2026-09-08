from fastapi import FastAPI
from typing_extensions import TypedDict
from pydantic import BaseModel
from collections.abc import Iterable, Sequence

class chatRequest(BaseModel):
    message: str
    temprature: float = 0.7


app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat(request: chatRequest):
    return {
        "message": request.message,
        "message_length": len(request.message),
        "temprature": request.temprature,
        "status": "received"        
    }

class User(TypedDict):
    name: str
    age: int
    height: float
    


@app.get("/get_user")
async def get_user(request: User):
    print(f"request: {request}")
    return {"status": "ok"}


def test_sequence(items: Sequence[str]):    
    print(f"item: {items[0]}")
    print(f"item len: {len(items)}")
    for item in items:
        print(item)

def test_iterable(items: Iterable[str]):
    print(f"item: {items[-1]}")
    print(f"item len: {len(items)}")
    for item in items:
        print(item)

# response = test_iterable(("Ali", "John"))
test_sequence(("Ali", "John"))

#list   => ["abc", "xyz", 123]
#tuple  => ("abc", 123)
#dict   => {"name" => "abc", "age" => 123}