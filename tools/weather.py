def get_weather(city: str):
    dummy_data = {
        "delhi": {"weather": "clear sky", "temp": 28, "humidity": 40},
        "mumbai": {"weather": "humid", "temp": 32, "humidity": 70},
        "london": {"weather": "cloudy", "temp": 18, "humidity": 60},
        "new york": {"weather": "rainy", "temp": 22, "humidity": 65}
    }

    city_lower = city.lower()

    if city_lower in dummy_data:
        data = dummy_data[city_lower]
        return f"🌦️ Weather in {city.title()}: {data['weather']}, 🌡️ Temp: {data['temp']}°C, 💧 Humidity: {data['humidity']}%"
    else:
        return f"❌ No data available for {city}"
