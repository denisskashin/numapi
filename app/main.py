import enum
import requests
from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com/"


class NotFound(str, enum.Enum):
    floor = "floor"
    ceil = "ceil"
    default = "default"


class DataType(str, enum.Enum):
    trivia = "trivia"
    math = "math"
    date = "date"
    year = "year"


@app.get("/")
def read_root():
    return {
        "Name": "Deniss Kashin",
        "Project": "Numbersapi test assignment",
        "Version": "0.0.1",
        "Time spent": "4 hours"
    }


@app.get("/fragment/{number}")
def fragment(number: int, data_type: DataType, default: Optional[str] = None,
             not_found: Optional[NotFound] = NotFound.default):
    request = f"{NUMBERS_API_URL}{number}/{data_type}?fragment&default={default}&not_found={not_found}&json"
    response = requests.get(request)
    return response.json()


@app.get("/fragment_date/{month}/{day}")
def fragment_date(month: int, day: int):
    response = requests.get(f"{NUMBERS_API_URL}{month}/{day}/date?json")
    return response.json()


@app.get("/random/{min}/{max}")
def random(min: int, max: int):
    response = requests.get(f"{NUMBERS_API_URL}random?min={min}&max={max}&json")
    return response.json()


@app.get("/batch/{numbers}")
def batch(numbers: str, data_type: Optional[DataType] = DataType.trivia):
    response = requests.get(f"{NUMBERS_API_URL}{numbers}/{data_type}?json")
    try:
        return response.json()
    except Exception as err:
        raise HTTPException(status_code=400, detail="Bad request")
