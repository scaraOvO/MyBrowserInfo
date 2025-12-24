from user_agents import parse


OS_ICON_MAP = {
    "mac": "macos",
    "windows": "windows",
    "linux": "linux",
    "android": "android",
    "ios": "ios",
}

BROWSER_ICON_MAP = {
    "brave": "brave",
    "arc": "arc",
    "vivaldi": "vivaldi",
    "chrome": "chrome",
    "firefox": "firefox",
    "safari": "safari",
    "edge": "edge",
}


def parse_ua(ua_string: str):
    ua = parse(ua_string)

    return {
        "os": f"{ua.os.family} {ua.os.version_string}",
        "browser": f"{ua.browser.family} {ua.browser.version_string}",
        "device": "Mobile" if ua.is_mobile else "Desktop",
    }


def icon_map(value: str, mapping: dict, fallback: str = "unknown"):
    if not value:
        return fallback

    v = value.lower()

    for key, icon in mapping.items():
        if key in v:
            return icon

    return fallback
