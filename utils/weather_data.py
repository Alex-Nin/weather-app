import logging
from .weather_reader import WeatherFileReader

class WeatherData:
    def __init__(self, file_reader: WeatherFileReader):
        self._file_reader = file_reader
        self._weather_data_df = None
        self.logger = logging.getLogger(__name__)


    def load_data(self):
        '''
        Loads the weather data using the provided file reader.

        Returns:
        The loaded pandas DataFrame or None if an error occurred.
        '''
        self.logger.info("Attempting to load weather data")
        try:
            self._weather_data_df = self._file_reader.read_file()
        except IOError as e:
            self.logger.error(f"IOError while loading weather data: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error while loading weather data: {str(e)}")
            raise
        if self._weather_data_df is None:
            self.logger.error("Failed to load weather data")
            raise RuntimeError("Failed to load weather data")
        self.logger.info("Weather data loaded successfully")
        return self._weather_data_df
        