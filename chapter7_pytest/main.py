def weather_check(temp:float)->str:
    print("Today's Weather News Are Like This...")
    msg = ''
    if temp <= 15:
        msg =  "Weather is freezing..."

    elif temp < 25:
        msg =  "Temperature is Pleasing today..."

    else:
        msg =  "Temperature is hot today..."

    print("Today's Temperature New Ends Here...")
    return msg


# news = weather_check(23)
# print(news)