from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.params import Query

app = FastAPI()


@app.get("/")
async def calculator(operation: str = Query(...), num1: int = Query(...), num2: int = Query(...)):
    result = None
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation specified.")

    return {"operation": operation, "num1": num1, "num2": num2, "result": result}

# To run the FastAPI app, save this file and run `uvicorn filename:app --reload` in your terminal.