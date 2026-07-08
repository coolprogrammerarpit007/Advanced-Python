from main import weather_check

# Test cases for weather check function

def test_weather_check():
    assert weather_check(-5) == "Weather is freezing..."
    assert weather_check(22) == "Temperature is Pleasing today..."
    assert weather_check(32) == "Temperature is hot today..."


if __name__ == "__main__":
    test_weather_check()