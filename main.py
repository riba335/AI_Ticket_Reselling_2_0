from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class EventInput(BaseModel):
    name: str
    date: str
    location: str
    price: float
    artist_popularity: int  # 0–100
    is_weekend: bool
    past_sales_success: float  # 0.0 – 1.0
    ticket_demand_score: int  # 0–100

class EventPrediction(BaseModel):
    attracti_score: float
    expected_profit: float
    should_buy: bool
    reason: str

@app.post("/predict", response_model=EventPrediction)
def predict_event(event: EventInput):
    attracti_score = (
        0.3 * event.artist_popularity +
        0.2 * (100 if event.is_weekend else 50) +
        0.3 * event.ticket_demand_score +
        0.2 * (event.past_sales_success * 100)
    )

    expected_selling_price = event.price * (1.2 + random.uniform(-0.1, 0.2))
    platform_fees = 0.1 * expected_selling_price
    expected_profit = round(expected_selling_price - event.price - platform_fees, 2)

    should_buy = attracti_score >= 70 and expected_profit > 5
    reason = "Vysoký dopyt a očakávaný zisk." if should_buy else "Nízka atraktivita alebo malý zisk."

    return EventPrediction(
        attracti_score=round(attracti_score, 2),
        expected_profit=expected_profit,
        should_buy=should_buy,
        reason=reason
    )

