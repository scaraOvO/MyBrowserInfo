import httpx


async def get_geo(ip: str):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get(f"http://ip-api.com/json/{ip}")
            data = r.json()

            return {
                "country": data.get("country"),
                "city": data.get("city"),
                "countryCode": data.get("countryCode"),
            }
    except Exception:
        return {
            "country": None,
            "city": None,
            "countryCode": None,
        }


def country_to_flag(code: str | None):
    if not code:
        return "🌍"
    return "".join(chr(127397 + ord(c)) for c in code.upper())
