import uvicorn
from fastapi import FastAPI


app= FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hellow World'}

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload = True)