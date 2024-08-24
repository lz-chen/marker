import logging
from flask import Flask, jsonify, request
import tempfile
from marker.convert import convert_single_pdf
from marker.models import load_all_models

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Marker service is running!"})

@app.route('/convert', methods=['POST'])
def convert():
    logging.info("Received request to /convert")
    file = request.files['file']
    model_lst = load_all_models()
    logging.info(f"Loaded models: {model_lst}")
    with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_pdf:
        temp_pdf.write(file.read())
        temp_pdf.seek(0)
        # Assuming convert_single_pdf is the function to convert PDF to markdown
        full_text, images, out_meta = convert_single_pdf(temp_pdf.name, [], None, False)
    logging.info("Conversion successful")
    return jsonify({"text": full_text, "metadata": out_meta})

@app.route('/favicon.ico')
def favicon():
    return '', 204
    logging.info("Starting Flask application")
    app.run(host='0.0.0.0', port=8000, threaded=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
