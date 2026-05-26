from fastapi import FastAPI

app = FastAPI()

@app.get("/format")
def format_weather(city: str = "Москва", temp: int = 20):
    return {
        "styled_text": f"Город: {city}. Погода: Отличная, {temp}°C!"
    }