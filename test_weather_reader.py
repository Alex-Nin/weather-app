import pytest
from unittest.mock import Mock
import pandas as pd
from io import StringIO
from utils.weather_data import WeatherData

MOCK_CSV_CONTENT = """MinTemp,MaxTemp,Rainfall
1,2,3
4,5,6
7,8,9
"""

@pytest.fixture
def mock_weather_reader():
    return Mock()

def test_weather_data_instantiation(mock_weather_reader):
    '''
    Test the instantiation of the WeatherData class
    '''
    weather_data = WeatherData(mock_weather_reader)
    assert weather_data is not None
    assert isinstance(weather_data, WeatherData)

def test_read_file_data(mock_weather_reader):
    '''
    Test the load_data method
    '''
    mock_df = pd.read_csv(StringIO(MOCK_CSV_CONTENT))
    mock_weather_reader.read_file.return_value = mock_df
    weather_data = WeatherData(mock_weather_reader)
    df = weather_data.load_data()
    
    assert df is not None
    assert not df.empty
    assert df.shape == (3, 3)
    assert list(df.columns) == ['MinTemp', 'MaxTemp', 'Rainfall']
    assert df['MinTemp'].tolist() == [1, 4, 7]
    assert df['MaxTemp'].tolist() == [2, 5, 8]
    assert df['Rainfall'].tolist() == [3, 6, 9]

def test_read_file_data_io_error(mock_weather_reader):
    '''
    Test the load_data method with an IOError
    '''
    mock_weather_reader.read_file.side_effect = IOError("Simulated IO error")
    weather_data = WeatherData(mock_weather_reader)
    with pytest.raises(IOError):
        weather_data.load_data()

def test_read_file_data_failed_to_read(mock_weather_reader):
    '''
    Test the load_data method with a RuntimeError
    '''
    mock_weather_reader.read_file.return_value = None
    weather_data = WeatherData(mock_weather_reader)
    with pytest.raises(RuntimeError):
        weather_data.load_data()