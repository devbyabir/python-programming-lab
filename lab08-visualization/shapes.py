import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle


def draw_shapes():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot([0.5, 2], [2.5, 3.5], color="tab:blue")
    ax.add_patch(Circle((3, 2.7), 0.6, color="tab:orange"))
    ax.add_patch(Rectangle((0.5, 0.5), 1.5, 0.8, color="tab:green"))
    ax.add_patch(Polygon([(3, 0.5), (4.5, 0.5), (4, 1.6)], color="tab:red"))
    ax.set(xlim=(0, 5), ylim=(0, 4), title="Basic shapes with Matplotlib")
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    figure = draw_shapes()
    if len(sys.argv) > 1:
        figure.savefig(sys.argv[1], dpi=150)
    else:
        plt.show()
    plt.close(figure)
