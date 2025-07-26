from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Event(BaseModel):
    name: str
    location: str
    price: float
    historical_sales: list[float]

@app.post("/analyze")
def analyze_event(event: Event):
    # Simulovaná analýza: vypočítame AttractiScore a odporúčanie nákupu
    trend = sum(event.historical_sales[-3:]) / 3 - sum(event.historical_sales[:3]) / 3
    score = min(max((trend * 10) + random.uniform(-5, 5), 0), 100)
    should_buy = score > 75 and event.price < 100

    # WhatsApp upozornenie - simulácia
    if should_buy:
        print(f"[WhatsApp SIMULATED] Výhodný lístok: {event.name} ({score:.1f}) €{event.price}")

    return {"AttractiScore": round(score, 1), "recommendation": "Buy" if should_buy else "Skip"}