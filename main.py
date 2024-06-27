import fastapi 
from pydantic import BaseModel
from typing import Union

app = fastapi.FastAPI()

class User(BaseModel):
    id: int
    email: str
    password: str  

@app.post("/users/{user}")
def create_user(user: int, id : int, email: str):
    return {"user created": user, "id": id, "email": email}

@app.get("/users/{user.id}")
def read_user(user: int, id : int, email : str,):
    return {"user": user, "id": id, "email": email}

@app.put("/users/{user}")
def update_user(user: int, id : int, email : str,):
    return {"message": "User updated successfully"}

@app.delete("/users/{user}")
def delete_user(id : int):
    return {"message": "User deleted"}