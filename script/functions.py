import simplekml
import os
from bs4 import BeautifulSoup


def read_from_path(data_path):
    # Read all files from data path
    file_paths = []
    file_names = []
    for path, _, filenames in os.walk(data_path):
        for name in filenames:
            file_paths.append(os.path.join(path, name))
            file_names.append(name)
    return file_paths, file_names

def data_template():
    return {
        'utc_datetime': None,
        'latitude': None,
        'longitude': None,
        'altitude': None,
        'bearing': None,
        'speed': None,
        'charging': None,
        'battery_level': None,
        'country': None,
        'provider': None,
        'foreground': None,
        'state': None,
        'scanning': None,
        'connected': None,
        'bssid': None,
        'rssi': None,
        'band': None,
        'channel': None
    }

def convert_file_to_dict(file_path, utc_date):
    f = open(file_path, 'r')
    soup = BeautifulSoup(f, 'html.parser')
    lines = soup.find_all('tr')
    dict_lines = []
    for line in lines[2:]:
        line_data = line.find_all('td')
        data_dict = data_template()
        for tagged_data, data_key in zip(line_data, data_dict.keys()):
            str_data = tagged_data.string
            if data_key == 'utc_datetime': # include data and time
                str_data = utc_date + ' ' + str_data
            data_dict[data_key] = str_data
            dict_lines.append(data_dict)
    f.close()
    return dict_lines
    
def save_day_kml(day, date):
    kml = simplekml.Kml()
    for line in day:
        location = line['country']
        latitude = line['latitude'].split(' ')[0]
        longitude = line['longitude'].split(' ')[0]
        altitude = line['altitude']
        timestamp = simplekml.TimeStamp(when=line['utc_datetime'])
        kml.newpoint(name = location, coords=[(latitude, longitude, altitude)], timestamp=timestamp)
    kml.save(f'./out/{date}.kml')

def save_all_kml(file_paths, file_names):
    kml = simplekml.Kml()
    for file_path, file_name in zip(file_paths, file_names):
        date = file_name.split('.')[0]
        day = convert_file_to_dict(file_path, date)
        for line in day:
            location = line['country']
            latitude = line['latitude'].split(' ')[0]
            longitude = line['longitude'].split(' ')[0]
            altitude = line['altitude']
            timestamp = simplekml.TimeStamp(when=line['utc_datetime'])
            kml.newpoint(name = location, coords=[(latitude, longitude, altitude)], timestamp=timestamp)
    kml.save('./out/all.kml')
