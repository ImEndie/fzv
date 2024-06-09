from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from index import solve

class FuncData(BaseModel):
    a: float
    b: float
    r: float
    h: float
    ort: float
    dast: float
    lyam: float
    sig_oquv: float
    p: float
    sxema: int


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/solve/")
async def solve_math(data: FuncData):
    print(data)
    try:
        data_dict=data.dict()
        print(data_dict.get("sxema"))
        r=solve(data_dict["a"],data_dict["b"],data_dict["r"],data_dict["h"],data_dict["ort"],data_dict["dast"],data_dict["lyam"],data_dict["sig_oquv"],data_dict["p"],data_dict.get("sxema"))
        print(r)
        return {
            "result": r
        }
    except Exception as e:
        print(e)
        return {
            "error": e
        }
