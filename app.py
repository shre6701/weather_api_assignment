import requests
import json


api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

# Function to fetch weather data from the API
def weather_data():
    try:
        response = requests.get(api_url)
        data = response.json()
        return data["list"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to get temperature for a specific date and time
def get_temp(data, target_date_time):
    for forecast in data:
        if forecast["dt_txt"] == target_date_time:
            return forecast["main"]["temp"]
    return None

# Function to get wind speed for a specific date and time
def get_windspeed(data, target_date_time):
    for forecast in data:
        if forecast["dt_txt"] == target_date_time:
            return forecast["wind"]["speed"]
    return None

# Function to get pressure for a specific date and time
def get_pre(data, target_date_time):
    for forecast in data:
        if forecast["dt_txt"] == target_date_time:
            return forecast["main"]["pressure"]
    return None

# Main program
if __name__ == "__main__":
    weather_data = weather_data()
    if weather_data is None:
        exit()

    while True:
        print("\nSelect an option:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your option: ")

        if option == "1":
            target_date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temp(weather_data, target_date_time)
            if temperature is not None:
                print(f"Temperature at {target_date_time}: {temperature}°C")
            else:
                print("No data found for the specified date and time.")

        elif option == "2":
            target_date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_windspeed(weather_data, target_date_time)
            if wind_speed is not None:
                print(f"Wind Speed at {target_date_time}: {wind_speed} m/s")
            else:
                print("No data found for the specified date and time.")

        elif option == "3":
            target_date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pre(weather_data, target_date_time)
            if pressure is not None:
                print(f"Pressure at {target_date_time}: {pressure} hPa")
            else:
                print("No data found for the specified date and time.")

        elif option == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please enter a valid option.")
