from flask import Flask, render_template, abort
import os
import time

STATIC_DIR = 'static'

app = Flask(__name__)

def get_files(path):
    path = os.path.normpath(path)
    if path.startswith('..'):
        path = path.lsplit('..')
    files = []
    if path not in ('/', '.'):
        files.append({
            'name': '..',
        })
    for f in os.listdir(STATIC_DIR + '/' + path):
        filename = f
        filestat = os.stat(STATIC_DIR + '/' + path + '/' + f)
        filesize = str(os.path.getsize(STATIC_DIR + '/' + path + '/' + f))
        last_modified = time.strftime('%Y-%m-%dT%H:%M:%SZ',
            time.gmtime(filestat.st_mtime))
        if os.path.isdir(STATIC_DIR + '/' + path + '/' + f):
            filename += '/'
            filesize = '-'
        files.append({
            'name': filename,
            'mode': oct(filestat.st_mode),
            'size': filesize,
            'last_modified': last_modified,
        })
    return files

@app.route('/')
def index():
    files = get_files('/')
    return render_template('index.html', path='/', files=files)

@app.route('/<path:path>')
def catch_all(path):
    print(STATIC_DIR + '/' + path)
    if not os.path.isdir(STATIC_DIR + '/' + path):
        abort(404)
    if os.path.isfile(STATIC_DIR + '/' + path):
        app.send_static_file(path)
    files = get_files(path)
    return render_template('index.html',
        path='/' + path,
        files=files)

if __name__ == '__main__':
    app.run(port=5000)

