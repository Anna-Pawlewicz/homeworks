# Napiszmy funkcję weather, która wydrukuje informacje o pogodzie przekazane jako parametry,
# np. \"Dziś w Gdańsku jest 12 stopni!\" \"Występuej duże zachmurzenie, wiatr wieje z prędkością 0\"
# #- miasto, temparatura, zachmurzenie, prędkość wiatru jako parametry wejściowe funcji,
# #wykorzystaj styl formatowania new lub f'string

# Napiszmy funkcję, która utworzy plik o nazawie weather.txt i do pliku wpisze parametry z zadania pierwszego \n",
# " - Napiszmy funkcję, która odczyta plik weather.txt oraz zwróci listę zaiwerającą weather_data = ['miasto', 'temparatura', 'zachmurzenie', 'predkocs_wiatru'],\n",
# " - Wywołujemy funkcję weather z elementami listy weather_data jako parametrami

# Dodatkowo przy okazji tych zadań proponuję poexperymentować np z używaniem innych typów
# do przechowywanie odczytanych danych( np słownik)


def weather(city, temperature, cloud_cover, wind_speed):
    print(f"Today in {city} is {temperature} degrees!\n"
          f"It's {cloud_cover}, the wind is blowing at speed {wind_speed}km/h.")


weather_data = ['Gdynia', 18.0, 'partly cloudy', 15]

weather(*weather_data)               # (weather_data[0], weather_data[1], weather_data[2], weather_data[3])


def create_file(file_name, city, temperature, cloud_cover, wind_speed):
    with open(file_name, 'w') as f:
        f.write(','.join([city, str(temperature), cloud_cover, str(wind_speed)])) # -> tworzymy listę ręcznie i zapisujemy ją za jednym razem sprawdzając czy wszystko to str


create_file('weather.txt', *weather_data)


def read_file(file_name):
    with open(file_name, 'r') as f:
        weather_data = f.read()
        return weather_data.split(',')


weather_data_return = read_file('weather.txt')
print(weather_data_return)

weather(*weather_data)

