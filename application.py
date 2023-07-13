from flask import Flask, request, jsonify
from services.utils import get_location_name, get_estimated_price

application = Flask(__name__)
app = application

@app.route('/get_location_name', methods=['GET'])
def get_location():
    location_names = get_location_name()
    return {"columns":location_names}, 200

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    datas = request.get_json()
    price = get_estimated_price(datas['location'], datas['sqft'], datas['bhk'], datas['bath'])
    return {"estimated_price":price}, 201


if __name__ == "__main__":
    app.run(port=80)
