<h1 align="center">📞 HCO-NumX Pro</h1>
<p align="center">An advanced phone number OSINT tool to reveal 60+ details using just a number.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Tool-HCO--NumX--Pro-darkgreen?style=for-the-badge&logo=target">
  <img src="https://img.shields.io/badge/Made%20for-Termux-blue?style=for-the-badge&logo=termux">
  <img src="https://img.shields.io/github/license/Hackerscolonyofficial/HCO-NumX-Pro?color=yellow&style=for-the-badge">
</p>

---

## 🌐 Hackers Colony Official Channels

<p align="center">
  <a href="https://www.instagram.com/hackers_colony_official"><img src="https://img.shields.io/badge/Instagram-Hackers%20Colony-critical?style=for-the-badge&logo=instagram"></a>
  <a href="https://www.facebook.com/share/1AY25it2Em/"><img src="https://img.shields.io/badge/Facebook-Hackers%20Colony-blue?style=for-the-badge&logo=facebook"></a>
  <a href="https://t.me/hackersColony"><img src="https://img.shields.io/badge/Telegram-Join%20Group-179cde?style=for-the-badge&logo=telegram"></a>
  <a href="https://discord.gg/Xpq9nCGD"><img src="https://img.shields.io/badge/Discord-Hackers%20Colony-5865F2?style=for-the-badge&logo=discord"></a>
  <a href="https://hackerscolonyofficial.blogspot.com/?m=1"><img src="https://img.shields.io/badge/Website-Hackers%20Colony-orange?style=for-the-badge&logo=googlechrome"></a>
</p>

---

## 🧠 What is HCO-NumX Pro?

> **HCO-NumX Pro** is an advanced OSINT tool that reveals 60+ data points about a phone number.  
You can also send a generated link to the victim — once they open it, you get full browser, device, and OS info in real-time on your local dashboard.

---

## ⚙️ Features

✅ Phone number intelligence (region, format, carrier)  
✅ Google search snippets  
✅ Basic Truecaller-style details  
✅ Victim IP, Browser, OS, Device  
✅ Real-time dashboard  
✅ Auto-starting Cloudflare tunnel  
✅ YouTube subscription gateway  
✅ Built for Termux

---

## 📲 Termux Setup (Step-by-Step)

```bash
# 1. Update Termux
pkg update && pkg upgrade -y

# 2. Install required packages
pkg install git python -y

# 3. Clone the tool
git clone https://github.com/Hackerscolonyofficial/HCO-NumX-Pro
cd HCO-NumX-Pro

# 4. Install Python dependencies
pip install -r requirements.txt

# 5. Run the tool
cd termux_tool
python main.py
```

---

## 🔐 Not a Free Tool

When you run the tool, it will display:

```
🔒 This is NOT a free tool!
🔗 Redirecting to our YouTube channel...
```

➡️ You will be redirected to subscribe to:  
**[Hackers Colony Tech on YouTube](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)**  
✅ After subscribing, return and press `Enter` to start the tool.

---

## 📡 How to Use

### ✅ Send the Link to Victim

After you press Enter, Termux will show a **Cloudflare public link**:
```
https://trycloudflare.com/xyz123
```

➡️ Send that link to the victim. When they open it, their device info will be logged silently.

---

### ✅ View Victim Info on Your Device

To view captured data (browser, OS, IP, etc.), open this in **your Android browser**:

```
http://127.0.0.1:5000/dashboard
```

⚠️ This link works only on the same device running the tool.

---

## 📸 Dashboard Preview

> Shows info like browser, OS, IP, and device type:

![preview](https://i.imgur.com/N7pzEwG.png)

---

## ⚠️ Disclaimer

This tool is intended for **educational and ethical research** purposes only.  
Misuse of this tool to target individuals without consent is strictly prohibited.  
The developers and Hackers Colony take **no responsibility** for any illegal use.

---

## 💬 Hacker Quote

> “The quieter you become, the more you are able to hear.”  
> — *Ram Dass*

---

## 👨‍💻 Code by Azhar

> Made with ❤️ by [Hackers Colony](https://github.com/Hackerscolonyofficial)  
> Subscribe: [YouTube – Hackers Colony Tech](https://youtube.com/@hackers_colony_tech)
