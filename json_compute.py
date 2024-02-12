import math
import json

with open('hand_movement_coordinates.json', 'r') as file:
    coordinates = json.load(file)


def calculate_mean_coordinates(coordinates):
    num_points = len(coordinates[0])

    mean_coordinates = []

    for i in range(num_points):
        sum_x = sum(coord[i]["x"] for coord in coordinates)
        sum_y = sum(coord[i]["y"] for coord in coordinates)

        mean_x = sum_x / len(coordinates)
        mean_y = sum_y / len(coordinates)

        mean_coordinates.append({"x": mean_x, "y": mean_y})

    return [mean_coordinates]


mean_skeleton = calculate_mean_coordinates(coordinates)
with open('mean_skeleton_coordinates.json', 'w') as file:
    json.dump(mean_skeleton, file)
