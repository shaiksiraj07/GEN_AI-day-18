
from typing import Union
import os
from fastapi import FastAPI, HTTPException

app = FastAPI()

BASE_PATH = "./user_files"

# Ensure the base directory exists
os.makedirs(BASE_PATH, exist_ok=True)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/create_directory/{dir_name}")
def create_directory(dir_name: str):
    dir_path = os.path.join(BASE_PATH, dir_name)
    
    try:
        os.makedirs(dir_path, exist_ok=True)
        return {"message": f"Directory '{dir_name}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating directory: {e}")

@app.post("/create_file/{dir_name}/{file_name}")
async def create_file(dir_name: str, file_name: str, content: Union[str, None] = None):
    dir_path = os.path.join(BASE_PATH, dir_name)
    
    if not os.path.exists(dir_path):
        raise HTTPException(status_code=404, detail=f"Directory '{dir_name}' not found.")
    
    file_path = os.path.join(dir_path, file_name)
    
    try:
        with open(file_path, "w") as file:
            if content:
                file.write(content)
        return {"message": f"File '{file_name}' created successfully in directory '{dir_name}'."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating file: {e}")
