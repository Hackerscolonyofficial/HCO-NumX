import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import requests
from urllib.parse import quote_plus

def lookup_number(number):
    try:
        parsed = phonenumbers.parse(number)
        valid = phonenumbers.is_valid_number(parsed)

        if not valid:
            return "<b>❌ Invalid phone number.</b>"

        # Number details
        country = geocoder.description_for_number(parsed, 'en')
        timezones = timezone.time_zones_for_number(parsed)
        sim_carrier = carrier.name_for_number(parsed, 'en')
        number_type = phonenumbers.number_type(parsed)

        if number_type == 1:
            line_type = "Mobile"
        elif number_type == 2:
            line_type = "Landline"
        elif number_type == 7:
            line_type = "VoIP"
        else:
            line_type = "Unknown"

        # Google search preview
        search_url = f"https://www.google.com/search?q={quote_plus(number)}"

        result = f"""
        <h3>📞 Phone Number Info:</h3>
        <ul>
            <li><b>Number:</b> {number}</li>
            <li><b>Valid:</b> ✅</li>
            <li><b>Country/Region:</b> {country}</li>
            <li><b>Timezone(s):</b> {', '.join(timezones)}</li>
            <li><b>Carrier:</b> {sim_carrier}</li>
            <li><b>Line Type:</b> {line_type}</li>
        </ul>

        <h4>🔎 Google Search:</h4>
        <a href="{search_url}" target="_blank">Search this number on Google</a>
        """

        return result

    except Exception as e:
        return f"<b>⚠️ Error:</b> {str(e)}"

def get_device_info(user_agent):
    # For now: just return basic info (extended info comes in Phase 2)
    return {
        "user_agent": user_agent,
        "is_mobile": "Mobile" in user_agent,
        "is_tablet": "Tablet" in user_agent,
        "is_pc": "Windows" in user_agent or "Linux" in user_agent,
    }
