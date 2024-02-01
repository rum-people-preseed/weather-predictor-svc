import prophet
import pandas as pd


async def get_temperature_next(date: str, temperature_data: pd.DataFrame, country: str, city: str) -> pd.DataFrame:
    

    processed_date = date + ' 00:00:00'
    indexes = temperature_data[temperature_data['ds'] == processed_date].index
    if indexes.size > 0:
        index = indexes[0] - 1
    else:
        index = len(temperature_data) 

    predictor = prophet.Prophet()
    predictor.fit(temperature_data.loc[:index])

    future = predictor.make_future_dataframe(periods=24, freq='H')
    forecast = predictor.predict(future)[['ds', 'yhat']]
    forecast['ds'] = forecast['ds'].map(lambda value: str(value))

    return forecast[-24:]