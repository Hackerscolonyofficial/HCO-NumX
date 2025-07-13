import requests

# 📡 Get geolocation & ISP info based on IP
def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,org,as,query,lat,lon,proxy")
        return response.json()
    except:
        return {}

# 📱 Extract basic user agent (browser/device)
def get_device_info(user_agent):
    return {
        "User-Agent": user_agent
    }

# 🔍 Dummy phone number lookup (extendable)
def lookup_number(number):
    # Future: Add Google scraping or API check
    return {
        "Number": number,
        "Valid": True,
        "Message": "Lookup logic can be added here."
    }
