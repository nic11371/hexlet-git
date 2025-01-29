import argparse
import requests
from polymorfizm.DIP.weather_service import WeatherService


def main(city_name):
    # BEGIN (write your solution here)
    weather = WeatherService(requests)
    ws = weather.look_up(city_name)
    return f"Temperature in {ws['name']}: {ws['temperature']}C"
    # END


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    print(main(args.city))
