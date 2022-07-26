import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_Estimated_price(location, sqrt, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqrt
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    load_saved_artifacts()
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open("./artifacts/banglore_home_prices_model.pickle", 'rb') as p:
        __model = pickle.load(p)
    print("loading saved artifacts..saved")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_Estimated_price('kalhalli', 1000, 2, 2))
    print(get_Estimated_price('amruthahalli', 1000, 2, 2))
