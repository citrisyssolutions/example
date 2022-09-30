python3 -m venv .venv
echo "Activating environment"
source .venv/bin/activate
echo "Starting application"
pip install -r requirements.txt
cd booking
#python app.py
gunicorn -b 0.0.0.0:5000 'app:app'