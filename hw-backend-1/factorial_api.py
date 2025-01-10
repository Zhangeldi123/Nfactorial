from fastapi import FastAPI 

app = FastAPI()

@app.get("/{num}")
def factorial(num: int):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return {"nfactorial": fact}