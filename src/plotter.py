import matplotlib.pyplot as plt
import io, base64
import os


def plot_temperature_day(place: str, temperature) -> str:
    '''
        This function plots temperature of the place for the day.
    '''
    x = temperature['ds'].map(lambda date: ':'.join(date.split(' ')[1].split(':')[:-1]))
    y = temperature['yhat']
    plt.figure().set_figwidth(8)
    plt.plot(x, y, '-', lw=0.5, color='C1')
    plt.xticks(rotation=45)
    plt.xlabel('Time, UTC',labelpad=10)
    plt.ylabel('Temperature, C')
    plt.axhline(0, color='black', lw=0.5)

    plt.title('Temperature for %s on %s' % (place, temperature['ds'].iloc[0].split(' ')[0]))
    plt.fill_between(list(range(24)), y, alpha=0.2, color=(252 / 255, 204 / 255, 0 / 255, 254 / 255))
    plt.xticks(range(0, 24, 3), x.iloc[::3])
    plt.show()

    image_bytes = io.BytesIO()
    plt.savefig(image_bytes, format='png')
    image_bytes.seek(0)

    return base64.encodebytes(image_bytes.read()).decode('utf-8')