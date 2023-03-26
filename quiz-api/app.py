from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def message():
	return f"Hello la E5FI"

if __name__ == "__main__":
    app.run()