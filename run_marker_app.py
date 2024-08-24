import argparse
import subprocess
import os


def run_app():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(cur_dir, "marker_app.py")
    cmd = ["streamlit", "run", app_path]
    try:
        subprocess.run(cmd, env={**os.environ, "IN_STREAMLIT": "true"}, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the app: {e}")


if __name__ == "__main__":
    run_app()
