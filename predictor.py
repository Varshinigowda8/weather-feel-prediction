from data import data

def predict_label(temp):
    # Find the closest temperature key
    closest_temp = min(data.keys(), key=lambda x: abs(x - temp))
    return data[closest_temp]
