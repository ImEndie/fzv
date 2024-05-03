from fastapi import FastAPI
from pydantic import BaseModel
from solve import solve


class FuncData(BaseModel):
    func1: str
    func2: str
    a: float
    b: float


app = FastAPI()


@app.post("/solve/")
async def solve_math(data: FuncData):
    data_dict=data.dict()
    r=solve(data_dict["func1"],data_dict["func2"],data_dict["a"],data_dict["b"])
    print(r)
    return {
        "r1": str(r[0]),
        "r2": str(r[1])
    }
