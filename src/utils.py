import prophet
from prophet.serialize import model_to_json, model_from_json
import pandas as pd
import os


async def get_temperature_next(date: str, temperature_data: pd.DataFrame, country: str, city: str) -> pd.DataFrame:
    if not os.path.exists('predictors'):
        os.mkdir('predictors')

    model_filename = os.path.join('predictors', '%s-%s.predictor' % (country, city))

    if os.path.exists(model_filename):
        with open(model_filename, 'r') as model:
            predictor = model_from_json(model.read())
    else:
        processed_date = date + ' 00:00:00'
        indexes = temperature_data[temperature_data['ds'] == processed_date].index
        if indexes.size > 0:
            index = indexes[0] - 1
        else:
            index = len(temperature_data) 

        predictor = prophet.Prophet()
        predictor.fit(temperature_data.loc[:index])

        with open(model_filename, 'w') as model:
            model.write(model_to_json(predictor))

    future = predictor.make_future_dataframe(periods=24, freq='H')
    forecast = predictor.predict(future)[['ds', 'yhat']]
    forecast['ds'] = forecast['ds'].map(lambda value: str(value))

    return forecast[-24:]