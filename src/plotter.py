import matplotlib.pyplot as plt
import os


async def plot_temperature_day(place: str, temperature) -> str:
    '''
        This function plots temperature of the place for the day.
    '''
    temp_dir_name = os.path.join('predictors', 'temp')
    image_name = os.path.join(temp_dir_name, '%s.png' % (place))

    if not os.path.exists(temp_dir_name):
        os.mkdir(temp_dir_name)

    if not os.path.exists(image_name):
        plt.plot(temperature['ds'], temperature['yhat'], '-o', marker='s')
        plt.xticks(rotation=45)
        plt.xlabel('Date, UTC',labelpad=10)
        plt.ylabel('Temperature, C')
        plt.title('Tomorrow\'s temperature for %s' % (place))
        plt.savefig(image_name, format='png')

    return image_name