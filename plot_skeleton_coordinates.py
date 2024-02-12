import json
import matplotlib.pyplot as plt

with open('hand_movement_coordinates.json', 'r') as data_file:
    data = json.load(data_file)
    x_coords = []
    y_coords = []
    for frame in data:
        for point in frame:
            x_coords.append(point['x'])
            y_coords.append(point['y'])

plt.plot(x_coords, y_coords)

plt.xlabel("X Coordinates")
plt.ylabel("Y Coordinates")
plt.title("Plot of x and y coordinates")

plt.show()
