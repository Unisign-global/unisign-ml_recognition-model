import math
import json

coordinates = [
    [
        {"x": 406, "y": 419, "timestamp": 1707742749.019096},
        {"x": 361, "y": 413, "timestamp": 1707742749.019096},
        {"x": 314, "y": 392, "timestamp": 1707742749.019096},
        {"x": 271, "y": 386, "timestamp": 1707742749.019096},
        {"x": 233, "y": 385, "timestamp": 1707742749.019096},
        {"x": 350, "y": 289, "timestamp": 1707742749.019096},
        {"x": 335, "y": 247, "timestamp": 1707742749.019096},
        {"x": 324, "y": 225, "timestamp": 1707742749.019096},
        {"x": 314, "y": 212, "timestamp": 1707742749.019096},
        {"x": 378, "y": 276, "timestamp": 1707742749.019096},
        {"x": 372, "y": 220, "timestamp": 1707742749.019096},
        {"x": 360, "y": 186, "timestamp": 1707742749.019096},
        {"x": 347, "y": 159, "timestamp": 1707742749.019096},
        {"x": 409, "y": 277, "timestamp": 1707742749.019096},
        {"x": 411, "y": 220, "timestamp": 1707742749.019096},
        {"x": 405, "y": 185, "timestamp": 1707742749.019096},
        {"x": 397, "y": 156, "timestamp": 1707742749.019096},
        {"x": 436, "y": 291, "timestamp": 1707742749.019096},
        {"x": 455, "y": 247, "timestamp": 1707742749.019096},
        {"x": 463, "y": 216, "timestamp": 1707742749.019096},
        {"x": 468, "y": 190, "timestamp": 1707742749.019096}
    ],
    [
        {"x": 418, "y": 428, "timestamp": 1707742749.047803},
        {"x": 367, "y": 416, "timestamp": 1707742749.047803},
        {"x": 316, "y": 393, "timestamp": 1707742749.047803},
        {"x": 269, "y": 385, "timestamp": 1707742749.047803},
        {"x": 232, "y": 384, "timestamp": 1707742749.047803},
        {"x": 351, "y": 290, "timestamp": 1707742749.047803},
        {"x": 329, "y": 248, "timestamp": 1707742749.047803},
        {"x": 318, "y": 228, "timestamp": 1707742749.047803},
        {"x": 307, "y": 214, "timestamp": 1707742749.047803},
        {"x": 379, "y": 276, "timestamp": 1707742749.047803},
        {"x": 369, "y": 219, "timestamp": 1707742749.047803},
        {"x": 356, "y": 184, "timestamp": 1707742749.047803},
        {"x": 344, "y": 156, "timestamp": 1707742749.047803},
        {"x": 409, "y": 277, "timestamp": 1707742749.047803},
        {"x": 408, "y": 218, "timestamp": 1707742749.047803},
        {"x": 402, "y": 183, "timestamp": 1707742749.047803},
        {"x": 394, "y": 153, "timestamp": 1707742749.047803},
        {"x": 438, "y": 291, "timestamp": 1707742749.047803},
        {"x": 457, "y": 247, "timestamp": 1707742749.047803},
        {"x": 467, "y": 216, "timestamp": 1707742749.047803},
        {"x": 473, "y": 188, "timestamp": 1707742749.047803}
    ]
]


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
