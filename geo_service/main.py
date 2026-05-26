from fastapi import FastAPI

app = FastAPI()

@app.get('/get_coordinats')
def get_coordinats(city: str = 'Moscow'):
    return {
        "status":  "success",
        "city": city,
        "lat": 55.75, 
        "lon": 37.61
    }
