import prophet
from prophet.serialize import model_to_json, model_from_json
import pandas as pd
import os
from datetime import datetime


def calculate_hours(last_date: str, date: str) -> int:
    print('Last date: ', last_date)
    print('Current date: ', date)

    last_datetime_obj = datetime.strptime(last_date, '%Y-%m-%d')
    current_datetime_obj = datetime.strptime(date, '%Y-%m-%d')
    delta = current_datetime_obj - last_datetime_obj

    return 24 * delta.days


async def get_temperature_next(date: str, temperature_data: pd.DataFrame, country: str, city: str) -> pd.DataFrame:
    if not os.path.exists('predictors'):
        os.mkdir('predictors')

    model_filename = os.path.join('predictors', '%s-%s %s.predictor' % (country, city, date))

    processed_date = date + ' 00:00:00'
    indexes = temperature_data[temperature_data['ds'] == processed_date].index
    if indexes.size > 0:
        index = indexes[0] - 1
    else:
        index = len(temperature_data) 

    if os.path.exists(model_filename):
        with open(model_filename, 'r') as model:
            predictor = model_from_json(model.read())
    else:

        predictor = prophet.Prophet()
        predictor.fit(temperature_data.loc[index - 365 * 24:index])

        with open(model_filename, 'w') as model:
            model.write(model_to_json(predictor))

    predict_hours = 24 if index != len(temperature_data) else calculate_hours(last_date=temperature_data.iloc[-1]['ds'].split(' ')[0], date=date)
    print('Predict hours: ', predict_hours)

    future = predictor.make_future_dataframe(periods=predict_hours, 
                                             freq='H')
    forecast = predictor.predict(future)[['ds', 'yhat']]
    forecast['ds'] = forecast['ds'].map(lambda value: str(value))

    return forecast[-24:]