import math

objects = [
    {"x": 0.5555680990219116, "y": 0.7437201738357544,
        "z": 0.7437201738357544, "timestamp": 1707730190.2958634},
    {"x": 0.6106155514717102, "y": 0.6627909541130066,
        "z": 0.6627909541130066, "timestamp": 1707730190.2958634}
]

euclidean_distances = [
    math.sqrt(obj['x']**2 + obj['y']**2 + obj['z']**2) for obj in objects]

sorted_objects = [obj for _, obj in sorted(zip(euclidean_distances, objects))]
median_index = len(sorted_objects) // 2

if len(sorted_objects) % 2 != 0:
    median_point = sorted_objects[median_index]
else:
    obj1 = sorted_objects[median_index - 1]
    obj2 = sorted_objects[median_index]
    median_point = {
        'x': (obj1['x'] + obj2['x']) / 2,
        'y': (obj1['y'] + obj2['y']) / 2,
        'z': (obj1['z'] + obj2['z']) / 2
    }

print("Median Point (x, y, z):", median_point)
