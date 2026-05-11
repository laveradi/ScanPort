from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/opt/render/project/src/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No filename', 400
    
    # Salva il file
    ip = request.remote_addr
    filename = f"{ip}_{file.filename}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    
    return 'OK', 200

@app.route('/')
def index():
    return 'Service Unavailable', 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)