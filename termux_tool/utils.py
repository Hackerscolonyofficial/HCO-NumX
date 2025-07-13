import requests

def get_device_info(user_agent):
    return {
        "User-Agent": user_agent
    }

def lookup_number(number):
    # Placeholder for number intelligence logic (Google search etc.)
    return {"number": number, "valid": True}

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,org,as,query,lat,lon,proxy")
        return response.json()
    except:
        return {}
