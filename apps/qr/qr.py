import os
import qrcode
from flask import Flask, request, render_template, Blueprint

qr = Blueprint("qr", __name__, static_folder="static", template_folder="templates")

@qr.route('/barcode', methods=['GET', 'POST'])
def barcode():
    if request.method == 'POST':
        link = request.form['link']
        QRGenerate = qrcode.make(link)
        
        safe_link = link.replace('http://', '').replace('https://', '').replace('/', '')
        qrSave = os.path.join('./apps/qr/static', f"{safe_link}.png")

        QRGenerate.save(qrSave)
        
        return render_template('qr.html', data=f"{safe_link}.png")
    return render_template('qr.html', data=None)