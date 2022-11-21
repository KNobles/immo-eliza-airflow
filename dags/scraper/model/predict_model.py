import pickle
import numpy as np

def predict(preprocessed_input):
    property_values = preprocessed_input
    with open("dags/scraper/model/immo_scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    
    with open("dags/scraper/model/immo_poly_features.pkl", "rb") as poly_features_file:
        poly_features = pickle.load(poly_features_file)
    
    with open("dags/scraper/model/immo_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    
    array_input = np.array([property_values])
    X_scaled_input = scaler.transform(array_input)
    price_prediction = model.predict(poly_features.fit_transform(X_scaled_input))
    return round(float(price_prediction), 2)