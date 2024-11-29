from flask import Flask
from qr import generate

app = Flask(__name__)

@app.route('/barcode', methods=['GET', 'POST'])
def barcode():
    return generate()

if __name__ == '__main__':
    app.run(debug=True)