from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
from datetime import datetime
from src import utils
from src import plotter

app = FastAPI()


@app.get('/')
async def test():
    return {'message': 'test connection!'}


@app.get('/temperature/')
async def predict_temperature(country: str | None = None, 
                          city: str | None = None,
                          latitude: str | None = None,
                          longtitude: str | None = None,
                          date: str | None = None):
    '''
        This endpoint predicts temperature on the next day.
    '''

    print('Parameters are: ', country, city, latitude, longtitude, date)
    data = pd.read_json('sample_json.json')
    data = data.sort_values(by=['timestamp'])
    data = data.rename(columns={
        'timestamp': 'ds',
        'temperature': 'y'
    })

    predicted = utils.get_temperature_next(date=date,
                                                 temperature_data=data,
                                                 country=country,
                                                 city=city)
    image_str = plotter.plot_temperature_day(place='%s, %s' % (country, city),
                                               temperature=predicted)

    return {
                'average_temperature': predicted['yhat'].sum() / 24,
                'chart': image_str
            }
