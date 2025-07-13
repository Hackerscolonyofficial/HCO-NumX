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

> **HCO-NumX Pro** is a powerful OSINT tool that fetches over 60 data points using just a phone number and victim interaction.  
You get full details like country, carrier, Truecaller-style name, social media info, device/browser data, and more.

---

## ⚙️ Features

✅ Phone Number Intelligence  
✅ Country, Carrier, Line Type  
✅ Google Reverse Lookup  
✅ Truecaller-like details  
✅ Victim IP + Location (if clicked)  
✅ Browser + OS + Device info  
✅ Clean dashboard  
✅ Cloudflared auto-tunnel  
✅ Termux-friendly  

---

## 📸 Dashboard Preview

> Instantly see victim info when they click your link:

![preview](https://i.imgur.com/N7pzEwG.png)

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

After running, it will show a Cloudflared link.  
👉 **Send that link to the victim.**

---

## 💻 Access Your Dashboard

Once someone opens the link, open this in your browser:

```
http://localhost:5000/dashboard
```

You'll see all device/browser info live.

---

## ⚠️ Disclaimer

This tool is made for **educational, research, and ethical hacking** purposes only.  
Any misuse is strictly your own responsibility.  
**Hackers Colony** and the developers do **not condone** illegal use.

---

## 💬 Hacker Quote

> “The quieter you become, the more you can hear.”  
> — *Ram Dass*

---

## 👨‍💻 Code by Azhar

> Made with ❤️ by **Hackers Colony**  
> Subscribe to our YouTube for more such tools and guides  
👉 [https://youtube.com/@hackers_colony_tech](https://youtube.com/@hackers_colony_tech)

---
