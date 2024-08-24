from flask import Flask, jsonify, request
import tempfile
from marker.convert import convert_single_pdf

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Marker service is running!"})

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_pdf:
        temp_pdf.write(file.read())
        temp_pdf.seek(0)
        # Assuming convert_single_pdf is the function to convert PDF to markdown
        full_text, images, out_meta = convert_single_pdf(temp_pdf.name, [], None, False)
    return jsonify({"text": full_text, "metadata": out_meta})

def run_app():
    app.run(host='0.0.0.0', port=8501)


if __name__ == "__main__":
    run_app()
