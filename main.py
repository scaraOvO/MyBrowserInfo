import os
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils.ua import parse_ua, icon_map, OS_ICON_MAP, BROWSER_ICON_MAP
from utils.geo import get_geo, country_to_flag

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

BACKGROUND_IMAGE = os.getenv("BACKGROUND_IMAGE", "")
SITE_TITLE = os.getenv("SITE_TITLE", "Visitor Info")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    ip = request.client.host
    ua_string = request.headers.get("user-agent", "")
    language = request.headers.get("accept-language", "")

    ua = parse_ua(ua_string)
    geo = await get_geo(ip)

    os_icon = icon_map(ua["os"], OS_ICON_MAP)
    browser_icon = icon_map(ua["browser"], BROWSER_ICON_MAP)

    visit = {
        "ip": ip,
        "country": geo.get("country"),
        "city": geo.get("city"),
        "flag": country_to_flag(geo.get("countryCode")),
        "visit_time": datetime.utcnow(),
        "language": language.split(",")[0],
        **ua,
        "os_icon": os_icon,
        "browser_icon": browser_icon,
    }
    
    if is_cli_request(ua_string):
        text = f"""Visitor Info
----------------
IP: {visit['ip']}
Location: {visit['country']} {visit['city']}
OS: {visit['os']}
Browser: {visit['browser']}
Device: {visit['device']}
Language: {visit['language']}
Time (UTC): {visit['visit_time']}
"""
        return PlainTextResponse(text)

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "v": visit,
            "bg": BACKGROUND_IMAGE,
            "title": SITE_TITLE,
        },
    )

def is_cli_request(user_agent: str) -> bool:
    ua = user_agent.lower()
    return any(k in ua for k in [
        "curl",
        "wget",
        "httpie",
        "go-http-client",
        "python-requests",
    ])
