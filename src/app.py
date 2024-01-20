from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)


def _fetch_machine_details():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return hostname, host_ip


@app.route("/details")
def details():
    hostname, host_ip = _fetch_machine_details()
    return render_template("index.html", hostname=hostname, host_ip=host_ip)


@app.route("/health")
def health():
    return jsonify(status="UP")


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
