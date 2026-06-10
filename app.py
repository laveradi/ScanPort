from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/uploads'  # ✅ path generico che funziona ovunque
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file', 400
    file = request.files['file']
    if file.filename == '':
        return 'No filename', 400
    ip = request.remote_addr
    filename = f"{ip}_{file.filename}"
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return 'OK', 200

@app.route('/')
def index():
    return 'OK', 200  # ✅ risponde 200, Railway è felice

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
