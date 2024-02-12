import json
import matplotlib.pyplot as plt


def plot_coordinates_from_json(json_files):
    plt.figure(figsize=(12, 6))

    for i, json_file in enumerate(json_files, start=1):
        with open(json_file, 'r') as data_file:
            data = json.load(data_file)
            for coordinates in data:
                x_coords = [point['x'] for point in coordinates]
                y_coords = [point['y'] for point in coordinates]

                plt.subplot(1, 2, i)
                if i == 1:
                    plt.title("individual skeleton coordinates")
                elif i == 2:
                    plt.title("mean skeletons coordinates")
                plt.plot(x_coords, y_coords)
                plt.xlabel("X")
                plt.ylabel("Y")

    plt.tight_layout()
    plt.show()


json_files = ['hand_movement_coordinates.json',
              'mean_skeleton_coordinates.json']
plot_coordinates_from_json(json_files)
