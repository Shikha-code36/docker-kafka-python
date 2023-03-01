from flask import Flask
from backend.producer import producer_bp

app = Flask(__name__)

app.register_blueprint(producer_bp, url_prefix='/producer')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
