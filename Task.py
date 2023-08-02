import requests

base_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# 1. for getting weather by date


def get_weather(date):
    response = requests.get(base_url)
    data = response.json()

    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']

    return None

# 2. for getting wind speed by data


def get_wind_speed(date):
    response = requests.get(base_url)
    data = response.json()

    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']

    return None

# 3. for getting pressure by date


def get_pressure(date):
    response = requests.get(base_url)
    data = response.json()

    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']

    return None

# main function :


def data():
    # while true loop is used because the program should not be terminated after performing any singular task and until the user press 0
    while True:
        # Data available from 2019-03-27 (18:00:00) to 2019-03-31 (17:00:00)
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temp = get_weather(date)
            if temp:
                print(f"Temperature on {date}: {temp}°C")
            else:
                print("Data is not available for the input date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data is not available for the input date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data is not available for the input date.")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    data()
