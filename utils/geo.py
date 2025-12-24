import httpx

async def get_geo(ip: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        return {
            "country": data.get("country"),
            "city": data.get("city")
        }
