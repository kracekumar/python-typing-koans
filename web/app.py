from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Code(BaseModel):
    text: str
    tags: list[str] = ['python']


@app.post('/type_check/')
async def type_check(code: Code):
    return {'status': 'success',
            'output': '',
            'error': '',
            'time_taken': ''}
