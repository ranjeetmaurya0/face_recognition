from flask import Flask, request, jsonify, render_template
from face_recognition import build_face_database, recognize
import os

app = Flask(__name__)
face_db = build_face_database('faces')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({"name": "No file uploaded"})

    file = request.files['image']
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    name = recognize(file_path, face_db)
    return jsonify({"name": name})

if __name__ == "__main__":
    dataset_path = r"C:\Users\Ranjeet Maurya\Downloads\archive (1)"
    
    face_db = build_face_database(dataset_path)
    test_image_path = r"C:\Users\Ranjeet Maurya\Downloads\archive (1)\Ranjeet\Image..jpg"
    result = recognize(test_image_path, face_db)
    print("Prediction:", result)
