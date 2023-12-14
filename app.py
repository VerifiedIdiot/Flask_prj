from flask import Flask
from flask_cors import CORS
from routes.weather import get_weather


app = Flask(__name__)
CORS(app, origins=['*'])


@app.route('/')
def home():
    return "This is Flask"

app.add_url_rule('/api/weather', 'get_weather', get_weather, methods=['GET'])
# app.add_url_rule('/api/strays', 'get_strays', get_strays, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)