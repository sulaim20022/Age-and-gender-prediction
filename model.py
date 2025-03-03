from tensorflow.keras.models import load_model

def load_trained_model():
    model = load_model("age_gender_model.h5", custom_objects={"mse": "mean_squared_error"})
    print("✅ Model loaded successfully!")
    return model
