import pickle
import pandas as pd

with open("model.pkl", 'rb') as file:
    pickle_model = pickle.load(file)
    file.close()

def predict_cost(features):
    if not features:
        return "Invalid request. Please provide a valid input."
    if not "Description" in features:
        return "Invalid request. Please provide a Description."
    if not "ModelYear" in features:
        return "Invalid request. Please provide a ModelYear."
    if not "Make" in features:
        return "Invalid request. Please provide a Make."
    if not "Model" in features:
        return "Invalid request. Please provide a Model."

    prediction = pickle_model.predict(pd.DataFrame([features]))

    return {
        "cost": prediction[0],
        "prediction": f"Estimated repair cost: ${prediction[0]:,.2f}"
    }
