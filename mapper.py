"""Coordinate helpers for the hospital indoor navigation model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable

import numpy as np


FLOOR_HEIGHT = 6.0


@dataclass(frozen=True)
class Location:
    """Represents a place in the building using 3D coordinates."""

    name: str
    x: float
    y: float
    z: int
    category: str

    @property
    def vector(self) -> np.ndarray:
        """Return the rendered 3D position for plotting and distance checks."""
        return np.array([self.x, self.y, self.z * FLOOR_HEIGHT], dtype=float)

    @property
    def floor_label(self) -> str:
        return f"Floor {self.z}"


def euclidean_distance(a: Location, b: Location) -> float:
    """3D Euclidean distance between two locations."""
    return float(np.linalg.norm(a.vector - b.vector))


def floor_shift(location: Location, target_floor: int) -> np.ndarray:
    """Project a location to another floor while preserving x/y coordinates."""
    transform = np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, FLOOR_HEIGHT * target_floor],
            [0.0, 0.0, 0.0, 1.0],
        ],
        dtype=float,
    )
    point = np.array([location.x, location.y, 0.0, 1.0], dtype=float)
    return transform @ point


def adjacency_matrix(locations: Dict[str, Location], edges: Iterable[tuple[str, str, float]]) -> np.ndarray:
    """Return a dense adjacency matrix for linear-algebra demonstrations."""
    names = list(locations)
    index = {name: idx for idx, name in enumerate(names)}
    matrix = np.full((len(names), len(names)), np.inf, dtype=float)
    np.fill_diagonal(matrix, 0.0)

    for source, destination, weight in edges:
        i = index[source]
        j = index[destination]
        matrix[i, j] = weight
        matrix[j, i] = weight

    return matrix