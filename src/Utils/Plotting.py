import matplotlib.pyplot as plt


def PlotPath(positions):
    xPositions, yPositions = zip(*positions)

    plt.figure(figsize=(8, 6))
    plt.plot(xPositions, yPositions, label="Object Path", color="blue")
    plt.scatter(xPositions[0], yPositions[0], color="green", label="Start", zorder=5)
    plt.scatter(xPositions[-1], yPositions[-1], color="red", label="End", zorder=5)
    plt.title("Object Trajectory")
    plt.xlabel("x Position")
    plt.ylabel("y Position")
    plt.legend()
    plt.grid(True)
    plt.show()
