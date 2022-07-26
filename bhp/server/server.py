from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_Estimated_price(location, sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python Flask Server for home price prediction...")
    app.run()
