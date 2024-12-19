import asyncio
from weather_data import WeatherData
from weather_statistics import WeatherStatistics
from weather_reader import WeatherFileReader
import logging
import os
import matplotlib.pyplot as plt
from functools import reduce

def stats_generator(stats):
    """
    Yields statistics from a list or single item.

    >>> list(stats_generator([1, 2, 3]))
    [1, 2, 3]
    
    >>> list(stats_generator(4))
    [4]
    """
    if isinstance(stats, list):
        for stat in stats:
            yield stat
    else:
        yield stats
        
def setup_logger():
    """
    Sets up the logger with a basic configuration.

    >>> isinstance(setup_logger(), logging.Logger)
    True
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

logger = setup_logger()

def plot_data(weather_data):
    """
    Visualizes the MinTemp and MaxTemp columns over time using matplotlib.
    """
    logger.info("Plotting weather data")

    plt.figure(figsize=(10, 5))
    
    # Plot MinTemp and MaxTemp over time
    plt.plot(weather_data['MinTemp'], label="MinTemp", color='blue')
    plt.plot(weather_data['MaxTemp'], label="MaxTemp", color='red')
    
    plt.xlabel("Days")
    plt.ylabel("Temperature (°C)")
    plt.title("Min and Max Temperatures Over Time")
    plt.legend()
    plt.show()

def filter_high_rainfall_days(data):
    """
    Filters for days where Rainfall is above 50mm using lambda and filter.

    >>> filter_high_rainfall_days([{'Rainfall': 60}, {'Rainfall': 20}])
    [{'Rainfall': 60}]
    """
    return list(filter(lambda day: day['Rainfall'] > 50, data))

async def main():
    logger.info("Starting weather data processing")
    csv_path = os.path.join(os.path.dirname(__file__), 'files', 'Weather Training Data.csv')

    # Step 1: Use WeatherFileReader to read the file asynchronously
    file_reader = WeatherFileReader(csv_path)

    # Step 2: Load the weather data using WeatherData (await the async call)
    weather_data = WeatherData(file_reader)
    data = await weather_data.load_data()

    if data is None:
        logger.error("Failed to load weather data. Exiting.")
        return

    # Step 3: Pass the data to WeatherStatistics for parallel calculation
    weather_stats = WeatherStatistics(data)
    stats = weather_stats.calculate_statistics()

    for stat in stats_generator(stats):
        print(stat)

    # Step 4: Plot data for visualization
    plot_data(data)

    # Step 5: Use map/reduce/filter functionality
    high_rainfall_days = filter_high_rainfall_days(data)
    total_rainfall = reduce(lambda acc, day: acc + day['Rainfall'], high_rainfall_days, 0)

    logger.info(f"Total rainfall on high rainfall days: {total_rainfall} mm")

    logger.info("Weather data processing completed")


if __name__ == '__main__':
    asyncio.run(main())