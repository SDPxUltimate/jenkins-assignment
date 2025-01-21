from fastapi import FastAPI

app = FastAPI()

@app.get("/getcode")
def get_code():
    return {"getcode": "kitton nimble no.1 55 ez xDxD"}

@app.get("/plus/{a}/{b}")
def plus(a: int, b: int):
    result = a + b
    return {"result": result}
