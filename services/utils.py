import json
import pickle
import numpy as np


__location = None
__data_column = None
__model = None



def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_column.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_column))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index  >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_name():
    # load_saved_artifacts()
    return __location

def load_saved_artifacts():
    global __location
    global __data_column
    global __model

    with open("./artifacts/column.json", 'r') as f:
        __data_column = json.load(f)['data_columns']
        __location = __data_column[3:]
    # print("loaded column name")
    with open("./artifacts/bangalore_home_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    # print("loaded model")

load_saved_artifacts()
if __name__ == "__main__":
    load_saved_artifacts()
    # print(get_location_name())
    print(get_estimated_price("1st Block Jayanagar", 1900, 3, 3))