def route_info(route):
    if 'distance' in route:
        distance = route['distance']
        return f"Distance to your destination is {distance}"
    elif 'speed' in route and 'time' in route:
        speed = route['speed']
        time = route['time']
        return f"Distance to your destination is {speed} * {time}"
    else:
        return "No distance info is available"


my_route = {
    'speed': 5,
    'time': 10,
}

print(route_info(my_route))
