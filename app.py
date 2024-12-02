from flask import Flask
from apps.qr.qr import qr

app = Flask(__name__)
app.register_blueprint(qr, url_prefix="/user")

@app.route('/')
def test():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)