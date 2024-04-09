from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city):
    api_key = 'a53aa0dd8f4ba8c1e2de8734dbc1fd3e'  
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather_data(city)
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
