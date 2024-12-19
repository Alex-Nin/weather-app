
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WeatherData(db.Model):
    __tablename__ = 'weather_data'
    
    id = db.Column(db.Integer, primary_key=True)
    # Default columns
    location = db.Column(db.String(100), nullable=True)
    min_temp = db.Column(db.Float, nullable=True)
    max_temp = db.Column(db.Float, nullable=True)
    rainfall = db.Column(db.Float, nullable=True)
    
    # Optional columns
    evaporation = db.Column(db.Float, nullable=True)
    sunshine = db.Column(db.Float, nullable=True)
    wind_gust_dir = db.Column(db.String(10), nullable=True)
    wind_gust_speed = db.Column(db.Float, nullable=True)
    wind_dir_9am = db.Column(db.String(10), nullable=True)
    wind_dir_3pm = db.Column(db.String(10), nullable=True)
    wind_speed_9am = db.Column(db.Float, nullable=True)
    wind_speed_3pm = db.Column(db.Float, nullable=True)
    humidity_9am = db.Column(db.Float, nullable=True)
    humidity_3pm = db.Column(db.Float, nullable=True)
    pressure_9am = db.Column(db.Float, nullable=True)
    pressure_3pm = db.Column(db.Float, nullable=True)
    cloud_9am = db.Column(db.Float, nullable=True)
    cloud_3pm = db.Column(db.Float, nullable=True)
    temp_9am = db.Column(db.Float, nullable=True)
    temp_3pm = db.Column(db.Float, nullable=True)
    rain_today = db.Column(db.String(5), nullable=True)
    rain_tomorrow = db.Column(db.Integer, nullable=True)

    def __init__(self, location, min_temp, max_temp, rainfall, 
             evaporation=None, sunshine=None, wind_gust_dir=None, 
             wind_gust_speed=None, wind_dir_9am=None, wind_dir_3pm=None,
             wind_speed_9am=None, wind_speed_3pm=None, humidity_9am=None,
             humidity_3pm=None, pressure_9am=None, pressure_3pm=None,
             cloud_9am=None, cloud_3pm=None, temp_9am=None, temp_3pm=None,
             rain_today=None, rain_tomorrow=None):
        # Default columns
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.rainfall = rainfall
        
        # Optional columns
        self.evaporation = evaporation
        self.sunshine = sunshine
        self.wind_gust_dir = wind_gust_dir
        self.wind_gust_speed = wind_gust_speed
        self.wind_dir_9am = wind_dir_9am
        self.wind_dir_3pm = wind_dir_3pm
        self.wind_speed_9am = wind_speed_9am
        self.wind_speed_3pm = wind_speed_3pm
        self.humidity_9am = humidity_9am
        self.humidity_3pm = humidity_3pm
        self.pressure_9am = pressure_9am
        self.pressure_3pm = pressure_3pm
        self.cloud_9am = cloud_9am
        self.cloud_3pm = cloud_3pm
        self.temp_9am = temp_9am
        self.temp_3pm = temp_3pm
        self.rain_today = rain_today
        self.rain_tomorrow = rain_tomorrow

    def __repr__(self):
        return f'<WeatherData location={self.location}, min_temp={self.min_temp}, max_temp={self.max_temp}, rainfall={self.rainfall}>'