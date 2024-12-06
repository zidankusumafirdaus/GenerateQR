import os
import qrcode
import hashlib
from flask import Flask, request, render_template, Blueprint, send_from_directory

qr = Blueprint("qr", __name__, static_folder="static", template_folder="templates")

FolderUploads = './apps/qr/uploads'
os.makedirs(FolderUploads, exist_ok=True)

@qr.route('/barcode', methods=['GET', 'POST'])
def barcode():
    if request.method == 'POST':
        # QR Code For URL
        link = request.form['link']
        QRGenerate = qrcode.make(link)

        safe_link = hashlib.md5(link.encode()).hexdigest() 
        qrSave = os.path.join(FolderUploads, f"{safe_link}.png")
        QRGenerate.save(qrSave)


        # QR Code For WhatsApp
        WhatsAppNumber = request.form['WhatsAppNumber']
        WhatsAppMessage = request.form['WhatsAppText']
        WhatsAppURL = f"https://wa.me/{WhatsAppNumber}?text={WhatsAppMessage}"
        

        
        return render_template('qr.html', data=f"{safe_link}.png")
    return render_template('qr.html', data=None)

@qr.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(FolderUploads, filename)