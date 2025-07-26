
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

CSV_PATH = "event_data.csv"

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    try:
        df = pd.read_csv(CSV_PATH)
    except Exception:
        df = pd.DataFrame(columns=["Názov", "Dátum", "Cena (€)", "Zisk (€)", "AttractiScore", "Odporúčanie"])
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": df.to_dict(orient="records")})

@app.post("/predict")
async def predict_event(request: Request):
    data = await request.json()
    cena = float(data.get("cena", 0))
    attract = int(data.get("attract_score", 0))

    odporucanie = "KÚPIŤ" if attract >= 75 and cena <= 100 else "NEKÚPIŤ"
    zisk = round(50 + attract - cena, 2)

    return {
        "expected_profit": zisk,
        "is_profitable": odporucanie == "KÚPIŤ",
        "attract_score": attract,
        "recommendation": odporucanie
    }
