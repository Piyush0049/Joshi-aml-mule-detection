import joblib
import pandas as pd

print("Load trained model and generate predictions.")

model = joblib.load("lightgbm_model.pkl")

# Example inference placeholder
print("Use model.predict_proba(features) to generate predictions.")