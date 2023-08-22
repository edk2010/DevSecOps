from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def get_hostname():
    hostname = socket.gethostname()
    response = f"<h1>Hello my dear friend</h1><h2>The hostname of this server is: </h2><h3>{hostname}</h3>"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)