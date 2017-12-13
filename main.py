from vr import app
from vr.model import base
from vr.controllers import index_controller
from flask import request, send_from_directory

@app.route('/visres/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run()
