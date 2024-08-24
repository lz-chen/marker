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
    max_pages = request.form.get('max_pages', default=None, type=int)
    langs = request.form.getlist('langs')
    if not langs:
        langs = ["English"]
    batch_multiplier = request.form.get('batch_multiplier', default=1, type=int)
    start_page = request.form.get('start_page', default=None, type=int)

    model_lst = load_all_models()
    logging.info(f"Loaded models: {model_lst}")
    with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_pdf:
        temp_pdf.write(file.read())
        temp_pdf.seek(0)
        # Assuming convert_single_pdf is the function to convert PDF to markdown
        full_text, images, out_meta = convert_single_pdf(temp_pdf.name, model_lst, max_pages=max_pages, langs=langs, batch_multiplier=batch_multiplier, start_page=start_page)
    logging.info("Conversion successful")
    return jsonify({"text": full_text, "metadata": out_meta})

@app.route('/favicon.ico')
def favicon():
    logging.info("Returning favicon")
    return '', 204


