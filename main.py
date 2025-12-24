from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

from db import visits
from utils.ua import parse_ua
from utils.geo import get_geo

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    ip = request.client.host
    ua_string = request.headers.get("user-agent", "")
    language = request.headers.get("accept-language", "")

    ua_info = parse_ua(ua_string)
    geo = await get_geo(ip)

    visit = {
        "ip": ip,
        "country": geo.get("country"),
        "city": geo.get("city"),
        "user_agent": ua_string,
        "language": language,
        "visit_time": datetime.utcnow(),
        **ua_info
    }

    visits.insert_one(visit)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "v": visit
        }
    )
