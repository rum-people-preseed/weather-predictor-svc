import matplotlib.pyplot as plt
import datetime


async def plot_temperature_day(place: str, start_date: str, end_date: str, temperature, format='%m/%d/%Y'):
    '''
        This function plots temperature of the place for the day.
    '''
    x = [start_date]
    next_date = start_date
    while next_date != end_date:
        date_object = datetime.datetime.strptime(next_date, format)
        next_date_object = date_object + datetime.timedelta(days=1)
        next_date = next_date_object.strftime(format)

        x.append(next_date)
    plt.plot(x[:-1], temperature, '-o', marker='s')
    plt.xticks(rotation=45)
    plt.xlabel('Date, UTC',labelpad=10)
    plt.ylabel('Temperature, C')
    plt.title('%s. Generated temperature for %s -- %s' % (place, start_date, end_date))
    plt.show()

    return 