def load_from_json():
    file = open("data.json")
    data = json.load(file)
    x = data['info']
    distance = x['distance']
    station = x['station']
    fuel = x['fuel']
    capacity = x['capacity']
    return distance, fuel, station, capacity