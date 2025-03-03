from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from model import load_trained_model

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load the trained model
model = load_trained_model()

# Function to preprocess images
def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    img = cv2.resize(img, (128, 128))  # Resize to model input shape
    img = img / 255.0  # Normalize pixel values (0-1)
    img = np.expand_dims(img, axis=-1)  # Add channel dimension (128, 128, 1)
    img = np.expand_dims(img, axis=0)   # Add batch dimension (1, 128, 128, 1)
    return img


# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Preprocess the image
            image = preprocess_image(filepath)

            # Predict age and gender
            predictions = model.predict(image)
            predicted_age = int(predictions[1][0][0])  # Age prediction
            predicted_gender = "Male" if predictions[0][0][0] > 0.5 else "Female"

            return render_template(
                "index.html",
                image_url=filepath,
                predicted_age=predicted_age,
                predicted_gender=predicted_gender,
            )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
