import matplotlib.pyplot as plt
import base64
from io import BytesIO


async def plot_temperature_day(place: str, temperature) -> BytesIO:
    '''
        This function plots temperature of the place for the day.
    '''
    plt.plot(temperature['ds'], temperature['yhat'], '-o', marker='s')
    plt.xticks(rotation=45)
    plt.xlabel('Date, UTC',labelpad=10)
    plt.ylabel('Temperature, C')
    plt.title('Tomorrow\'s, temperature for %s' % (place))

    figure = plt.figure()
    figure.canvas.draw()
    bytestream = BytesIO()
    figure.savefig(bytestream, format='png')
    bytestream.seek(0)
    image = base64.encodebytes(bytestream.read()).decode('utf-8')

    return image