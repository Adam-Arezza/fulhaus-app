from flask import Flask, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model("fulhaus_model.h5")
class_map = ["Bed", "Chair", "Sofa"]
app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict_image():
    if request.method == "POST":
        try:
            file = request.files.get("imageFile").read()
            image = np.fromstring(file, np.uint8)
            img = cv2.imdecode(image,cv2.IMREAD_COLOR)
            resized = cv2.resize(img, (256, 256))
            resized = resized * (1.0 / 255.0)
            resized = np.array([resized])
            classification = np.argmax(model.predict(resized))
            return class_map[classification]

        except Exception as e:
            print(e)
            return "FAIL"
        
if (__name__ == "__main__"):
    app.run()