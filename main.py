from fastapi import FastAPI
import pandas as pd
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
    data = pd.read_csv('./data/weatherHistory-processed.csv')

    predicted = await utils.get_temperature_next(date=date,
                                                 temperature_data=data,
                                                 country=country,
                                                 city=city)
    chart = await plotter.plot_temperature_day(place='%s, %s' % (country, city),
                                               temperature=predicted)

    return {
                'average_temperature': predicted['yhat'].sum() / 24,
                'chart': chart
            }


@app.get('/chart/')
async def get_chart(country: str | None = None,
                    city: str | None = None,
                    latitude: str | None = None, 
                    longtitude: str | None = None,
                    date: str | None = None):
    data = pd.read_csv('data/weatherHistory-processed.csv')
    predicted = await utils.get_temperature_next(date=date,
                                           temperature_data=data)
    chart = await plotter.plot_temperature_day()
    
    return 
