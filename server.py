import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World!'

@app.route('/files/<path:path>')
def send_file(path):
    print("Sending Fron " + str(path))
    return send_from_directory('files', path)

if __name__ == '__main__':
    os.system("chrome http://localhost:5000")
    app.run()