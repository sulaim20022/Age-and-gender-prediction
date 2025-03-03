# Age and Gender Prediction using CNN

## Overview
This project implements a Convolutional Neural Network (CNN) model for age and gender prediction using the UTKFace dataset. It allows users to upload an image and get predictions for age and gender. A Flask web application is used to serve the model and provide an interface for users.

## Features
- Predicts age and gender from an uploaded image.
- Uses a trained CNN model.
- Web interface built using Flask.
- Simple UI for easy user interaction.

## Dataset
- **UTKFace Dataset**: The dataset contains images of human faces labeled with age, gender, and ethnicity.
- Images are preprocessed before feeding into the CNN model.

## Technologies Used
- **Python**
- **Flask** (for web application)
- **TensorFlow/Keras** (for CNN model)
- **OpenCV** (for image processing)
- **HTML, CSS, JavaScript** (for frontend)

## Installation Guide
1. **Clone the repository**
   ```sh
   git clone https://github.com/sulaim20022/Age-and-gender-prediction.git
   cd Age-and-gender-prediction
   ```
2. **Set up a virtual environment**
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Download the pre-trained model**
   - Place the `age_gender_model.h5` file in the project directory.

## Running the Application
1. **Start the Flask server**
   ```sh
   python app.py
   ```
2. **Open in browser**
   - Go to `http://127.0.0.1:5000/` to access the web app.

## File Structure
```
Age-and-gender-prediction/
│-- app.py                 # Main Flask app
│-- model.py               # CNN model architecture and loading
│-- age_gender_model.h5    # Trained model
│-- requirements.txt       # Dependencies
│-- templates/
│   ├── index.html         # Frontend UI
│-- static/
│   ├── styles.css         # CSS for styling
```

## Deployment
To deploy on **GitHub**, ensure large files are handled correctly:
```sh
git lfs install
git lfs track "*.h5"
git add .
git commit -m "Initial commit"
git push origin main
```

## Troubleshooting
- **Large file errors**: Use Git LFS for files over 50MB.
- **Virtual environment issues**: Ensure `myenv` is activated before running the app.
- **Model shape errors**: Ensure input image is resized to the expected dimensions (128x128x1).

## Future Improvements
- Improve model accuracy with more training data.
- Deploy on a cloud platform (Heroku, AWS, etc.).
- Add real-time webcam-based predictions.

## Contributors
- **Muhammed Sulaim**



