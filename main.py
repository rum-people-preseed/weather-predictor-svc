from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def test():
    return {'message': 'test connection!'}


@app.get('/temperature/{day}')
async def get_temperature(day: str):
    return {'day': day, 'temperature': 0}


@app.get('/chart/{period}')
async def get_chart(period: str):
    return {'chart': bytes([])}
