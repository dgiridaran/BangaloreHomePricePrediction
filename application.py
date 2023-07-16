from flask import Flask, request, jsonify, render_template, url_for
from services.utils import get_location_name, get_estimated_price

application = Flask(__name__)
app = application

@app.route('/get_location_name', methods=['GET'])
def get_location():
    location_names = get_location_name()
    return {"columns":location_names}, 200

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
        # print(data)
        # datas = request.get_json()
        datas = {'location':data['location'][0], 'sqft':int(data['sqft'][0]), 'bhk':int(data['bhk'][0]), 'bath':int(data['bath'][0])}
        price = get_estimated_price(datas['location'], datas['sqft'], datas['bhk'], datas['bath'])
        # return {"estimated_price":price}, 201
        return render_template('predictin.html', price=str(price), location_dropdown = get_location_name(), bhk=datas['bhk'])
    if request.method == 'GET':
        return render_template('predictin.html', location_dropdown = get_location_name())

@app.route('/', methods=['GET'])
def home():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(port=80, debug=True)
