"""3D plotting for the hospital navigation graph and selected route."""

from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

from mapper import FLOOR_HEIGHT, Location


CATEGORY_COLORS = {
    "entry": "#1d4ed8",
    "service": "#0891b2",
    "corridor": "#64748b",
    "ward": "#16a34a",
    "diagnostics": "#f59e0b",
    "critical": "#dc2626",
    "lift": "#7c3aed",
    "stairs": "#ea580c",
}


def plot_hospital_route(
    locations: Dict[str, Location],
    edges: Iterable[Tuple[str, str, float]],
    path: List[str],
) -> None:
    """Display the hospital graph and highlight the chosen route."""
    figure = plt.figure(figsize=(11, 8))
    axis = figure.add_subplot(111, projection="3d")

    floors = sorted({location.z for location in locations.values()})
    x_values = [location.x for location in locations.values()]
    y_values = [location.y for location in locations.values()]

    for floor in floors:
        z = floor * FLOOR_HEIGHT
        axis.plot(
            [min(x_values) - 1, max(x_values) + 1, max(x_values) + 1, min(x_values) - 1, min(x_values) - 1],
            [min(y_values) - 1, min(y_values) - 1, max(y_values) + 1, max(y_values) + 1, min(y_values) - 1],
            [z, z, z, z, z],
            color="#cbd5e1",
            linestyle="--",
            linewidth=0.8,
        )
        axis.text(min(x_values) - 1, max(y_values) + 1.2, z, f"Floor {floor}", color="#334155")

    for source, destination, _weight in edges:
        start = locations[source].vector
        end = locations[destination].vector
        axis.plot(
            [start[0], end[0]],
            [start[1], end[1]],
            [start[2], end[2]],
            color="#cbd5e1",
            linewidth=1.2,
            alpha=0.9,
        )

    for location in locations.values():
        color = CATEGORY_COLORS.get(location.category, "#0f172a")
        axis.scatter(location.x, location.y, location.vector[2], color=color, s=80)
        axis.text(location.x + 0.12, location.y + 0.12, location.vector[2] + 0.2, location.name, fontsize=8)

    route_points = [locations[name].vector for name in path]
    axis.plot(
        [point[0] for point in route_points],
        [point[1] for point in route_points],
        [point[2] for point in route_points],
        color="#ef4444",
        linewidth=3.2,
        marker="o",
        markersize=7,
        label="Shortest path",
    )

    axis.set_title("PathMatrix 3D Hospital Navigation")
    axis.set_xlabel("X axis")
    axis.set_ylabel("Y axis")
    axis.set_zlabel("Height / Floor")
    axis.legend()
    plt.tight_layout()
    plt.show()
