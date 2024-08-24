from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Marker service is running!"})

def run_app():
    app.run(host='0.0.0.0', port=8501)


def run_app():
    # Implement the service logic here
    print("Running marker service...")
    # Add the necessary code to start your service


if __name__ == "__main__":
    run_app()
