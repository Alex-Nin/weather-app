
import pandas as pd
import logging

class WeatherStatistics:
    def __init__(self, weather_data):
        self.weather_data = pd.DataFrame([
            {'MinTemp': w.min_temp, 'MaxTemp': w.max_temp, 'Rainfall': w.rainfall}
            for w in weather_data
        ])
        self.logger = logging.getLogger(__name__)

    def calculate_statistics(self):
 
        min_temp_avg = self.weather_data['MinTemp'].mean()
        max_temp_avg = self.weather_data['MaxTemp'].mean()
        rainfall_total = self.weather_data['Rainfall'].sum()
        return f"Avg Min Temp: {min_temp_avg}, Avg Max Temp: {max_temp_avg}, Total Rainfall: {rainfall_total}"
