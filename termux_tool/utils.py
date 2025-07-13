```python
import phonenumbers
import requests
from bs4 import BeautifulSoup
from user_agents import parse

def lookup_number(number):
    info = {}

    try:
        parsed = phonenumbers.parse(number)
        info["Valid"] = phonenumbers.is_valid_number(parsed)
        info["International Format"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        info["Local Format"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
        info["Country"] = phonenumbers.region_code_for_number(parsed)
        info["Carrier"] = phonenumbers.carrier.name_for_number(parsed, "en")
        info["Time Zone"] = ", ".join(phonenumbers.timezone.time_zones_for_number(parsed))
    except:
        info["Error"] = "Invalid phone number format"

    try:
        # Google search for public info
        q = requests.get(f"https://www.google.com/search?q={number}", headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(q.text, "html.parser")
        search_snippets = [i.text for i in soup.select("div.BNeawe.vvjwJb.AP7Wnd")][:3]
        info["Google Snippets"] = search_snippets if search_snippets else "No public results"
    except:
        info["Google Snippets"] = "Lookup failed"

    return info

def get_device_info(user_agent_string):
    ua = parse(user_agent_string)
    return {
        "Browser": ua.browser.family + " " + str(ua.browser.version_string),
        "OS": ua.os.family + " " + str(ua.os.version_string),
        "Device": ua.device.family,
        "Is Mobile": ua.is_mobile,
        "Is PC": ua.is_pc,
        "Is Tablet": ua.is_tablet,
        "User-Agent": user_agent_string
    }
```
