from user_agents import parse

def parse_ua(ua_string: str):
    ua = parse(ua_string)
    return {
        "os": f"{ua.os.family} {ua.os.version_string}",
        "browser": f"{ua.browser.family} {ua.browser.version_string}",
        "device": "Mobile" if ua.is_mobile else "Tablet" if ua.is_tablet else "PC",
        "arch": "arm" if "arm" in ua_string.lower() else "x86_64"
    }
