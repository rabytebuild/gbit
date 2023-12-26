from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    num_visitors = int(request.form['num_visitors'])
    ips = []
    countries = []
    devices = []

    for _ in range(num_visitors):
        ip = request.form.get('ip') or random.choice(["192.168.0.1", "172.16.0.1"])
        ips.append(ip)
        countries.append(request.form.get('country') or "")
        devices.append(request.form.get('device') or "")

    return render_template('result.html', visitors=zip(ips, countries, devices))

if __name__ == '__main__':
    app.run(debug=True)
