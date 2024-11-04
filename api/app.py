from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional
import os
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI(description="TP5 API")

@app.get
def root():
    return {}

@app.get("/")
def root():
    return {"message": "TP5 API"}

@app.get("/addition")
def addition(a: Optional[float] = 0, b: Optional[float] = 0):
    if a is None or b is None:
        raise HTTPException(status_code=400, detail="Both query parameters 'a' and 'b' are required")
    return {"result": a + b}
# exemple : /addition?a=5&b=10

@app.get("/user")
def read_user(username: str):
    for file in os.listdir("data"):
        if file == username:
            return {"username": username}

@app.get("/createuser")
def create_user(username: str):
    with open(f"data/{username}", "w") as file:
        print("Entré nom d'utilisateur")
        username = input()
        print("Entré votre to do list")
        todolist = input()
        file.write(f"{username} : {todolist}")
    return {"username": username}

@app.get("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"username": form_data.username}