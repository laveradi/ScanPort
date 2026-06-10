from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/uploads'
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

@app.route('/files')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    if not files:
        return 'Nessun file caricato.'
    links = [f'<a href="/files/{f}">{f}</a>' for f in files]
    return '<br>'.join(links)

@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/')
def index():
    return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
