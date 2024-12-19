# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from functools import wraps
from models import db, WeatherData
from utils.weather_reader import WeatherFileReader
from utils.weather_data import WeatherData as WeatherDataClass
from utils.weather_statistics import WeatherStatistics
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

app.secret_key = '0000' 
CORRECT_PASSWORD = 'pythonisfun'

@app.before_request
def create_tables():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authenticated' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == CORRECT_PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Incorrect password")
    return render_template('login.html')


@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/load-data', methods=['GET'])
@login_required
def load_data():
    file_path = os.path.join('data', 'Weather Training Data1.csv')
    reader = WeatherFileReader(file_path)
    weather_data = WeatherDataClass(reader)
    
    try:
        data = weather_data.load_data()
        
        skipped_rows = 0
        added_rows = 0
        
        for _, row in data.iterrows():
            try:
                weather_entry = WeatherData(
                    # Default columns
                    location=str(row['Location']) if 'Location' in row else None,
                    min_temp=float(row['MinTemp']) if row['MinTemp'] else None,
                    max_temp=float(row['MaxTemp']) if row['MaxTemp'] else None,
                    rainfall=float(row['Rainfall']) if row['Rainfall'] else None,
                    
                    # Optional columns
                    evaporation=float(row['Evaporation']) if row['Evaporation'] else None,
                    sunshine=float(row['Sunshine']) if row['Sunshine'] else None,
                    wind_gust_dir=str(row['WindGustDir']) if row['WindGustDir'] else None,
                    wind_gust_speed=float(row['WindGustSpeed']) if row['WindGustSpeed'] else None,
                    wind_dir_9am=str(row['WindDir9am']) if row['WindDir9am'] else None,
                    wind_dir_3pm=str(row['WindDir3pm']) if row['WindDir3pm'] else None,
                    wind_speed_9am=float(row['WindSpeed9am']) if row['WindSpeed9am'] else None,
                    wind_speed_3pm=float(row['WindSpeed3pm']) if row['WindSpeed3pm'] else None,
                    humidity_9am=float(row['Humidity9am']) if row['Humidity9am'] else None,
                    humidity_3pm=float(row['Humidity3pm']) if row['Humidity3pm'] else None,
                    pressure_9am=float(row['Pressure9am']) if row['Pressure9am'] else None,
                    pressure_3pm=float(row['Pressure3pm']) if row['Pressure3pm'] else None,
                    cloud_9am=float(row['Cloud9am']) if row['Cloud9am'] else None,
                    cloud_3pm=float(row['Cloud3pm']) if row['Cloud3pm'] else None,
                    temp_9am=float(row['Temp9am']) if row['Temp9am'] else None,
                    temp_3pm=float(row['Temp3pm']) if row['Temp3pm'] else None,
                    rain_today=str(row['RainToday']) if row['RainToday'] else None,
                    rain_tomorrow=int(row['RainTomorrow']) if row['RainTomorrow'] else None
                )
                db.session.add(weather_entry)
                added_rows += 1
                
            except (KeyError, ValueError) as e:
                print(f"Error processing row: {row}")
                return jsonify({"error": f"Error processing row: {str(e)}"})
                
        db.session.commit()
        return jsonify({
            "status": "Data loaded successfully",
            "rows_added": added_rows,
            "rows_skipped": skipped_rows
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

# Add this to your Flask route that renders the template
@app.route('/list-data', methods=['GET'])
@login_required
def list_data():
    data = WeatherData.query.all()
    statistics = WeatherStatistics(data).calculate_statistics()
    
    # Define column configurations - use lowercase to match model attributes
    default_columns = ['location', 'min_temp', 'max_temp', 'rainfall']
    optional_columns = [
        'evaporation', 'sunshine', 'wind_gust_dir', 'wind_gust_speed',
        'wind_dir_9am', 'wind_dir_3pm', 'wind_speed_9am', 'wind_speed_3pm',
        'humidity_9am', 'humidity_3pm', 'pressure_9am', 'pressure_3pm',
        'cloud_9am', 'cloud_3pm', 'temp_9am', 'temp_3pm',
        'rain_today', 'rain_tomorrow'
    ]
    
    return render_template('list_data.html', 
                         data=data, 
                         statistics=statistics,
                         default_columns=default_columns,
                         optional_columns=optional_columns)

if __name__ == '__main__':
    app.run(debug=True)
