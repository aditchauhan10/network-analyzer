import os
import subprocess
import sys

# Streamlit app file path
app_path = os.path.join(os.path.dirname(__file__), "app.py")
subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])
