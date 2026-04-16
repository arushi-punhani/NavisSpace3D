"""Pathfinding helpers for the hospital navigation system."""

from __future__ import annotations

from typing import Dict, List

import networkx as nx

from mapper import Location, euclidean_distance


def _heuristic(current: str, target: str, locations: Dict[str, Location]) -> float:
    return euclidean_distance(locations[current], locations[target])


def find_shortest_path(
    graph: nx.Graph,
    locations: Dict[str, Location],
    source: str,
    destination: str,
    algorithm: str = "dijkstra",
) -> tuple[List[str], float]:
    """Compute the shortest route using Dijkstra or A*."""
    if source not in graph or destination not in graph:
        raise ValueError("Source or destination does not exist in the hospital map.")

    algorithm = algorithm.lower().strip()
    if algorithm == "dijkstra":
        path = nx.dijkstra_path(graph, source, destination, weight="weight")
    elif algorithm in {"astar", "a*"}:
        path = nx.astar_path(
            graph,
            source,
            destination,
            heuristic=lambda a, b: _heuristic(a, b, locations),
            weight="weight",
        )
    else:
        raise ValueError("Algorithm must be either 'dijkstra' or 'astar'.")

    distance = nx.path_weight(graph, path, weight="weight")
    return path, float(distance)


def describe_route(path: List[str], locations: Dict[str, Location]) -> List[str]:
    """Generate user-friendly step descriptions for the route."""
    steps: List[str] = []
    for current, nxt in zip(path, path[1:]):
        current_location = locations[current]
        next_location = locations[nxt]

        if current_location.z != next_location.z:
            movement = "Take the lift" if "Lift" in current or "Lift" in nxt else "Use the stairs"
            steps.append(
                f"{movement} from {current_location.floor_label} to {next_location.floor_label} via {nxt}."
            )
        else:
            steps.append(f"Move from {current} to {nxt} on {current_location.floor_label}.")

    return steps
