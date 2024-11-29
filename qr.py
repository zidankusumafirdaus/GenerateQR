import os
import qrcode
from flask import Flask, request, render_template

app = Flask(__name__)

def generate():
    if request.method == 'POST':
        link = request.form['link']
        qr = qrcode.make(link)
        
        safe_link = link.replace('http://', '').replace('https://', '').replace('/', '')
        qrSave = os.path.join('static', f"{safe_link}.png")
        
        qr.save(qrSave)
        
        return render_template('qr.html', data=qrSave)
    return render_template('qr.html', data=None)