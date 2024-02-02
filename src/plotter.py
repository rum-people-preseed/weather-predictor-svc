import matplotlib.pyplot as plt
import io, base64
import os


async def plot_temperature_day(place: str, temperature) -> str:
    '''
        This function plots temperature of the place for the day.
    '''
    plt.plot(temperature['ds'], temperature['yhat'], '-o', marker='s')
    plt.xticks(rotation=45)
    plt.xlabel('Date, UTC',labelpad=10)
    plt.ylabel('Temperature, C')
    plt.title('Tomorrow\'s temperature for %s' % (place))

    image_bytes = io.BytesIO()
    plt.savefig(image_bytes, format='png')
    image_bytes.seek(0)

    return base64.encodebytes(image_bytes.read()).decode('utf-8')