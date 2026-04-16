"""Create a sample 3D graph for a hospital building."""

from __future__ import annotations

from typing import Dict, List, Tuple

import networkx as nx

from mapper import Location, euclidean_distance


def _build_locations() -> Dict[str, Location]:
    return {
        "Entrance": Location("Entrance", 0, 2, 0, "entry"),
        "Reception": Location("Reception", 2, 2, 0, "service"),
        "Emergency": Location("Emergency", 5, 1, 0, "ward"),
        "Pharmacy": Location("Pharmacy", 8, 2, 0, "service"),
        "Hall A": Location("Hall A", 4, 4, 0, "corridor"),
        "Lift G": Location("Lift G", 6, 5, 0, "lift"),
        "Stairs G": Location("Stairs G", 1, 6, 0, "stairs"),
        "Hall B": Location("Hall B", 4, 4, 1, "corridor"),
        "Radiology": Location("Radiology", 7, 2, 1, "diagnostics"),
        "Lab": Location("Lab", 8, 6, 1, "diagnostics"),
        "Ward 101": Location("Ward 101", 2, 1, 1, "ward"),
        "Lift 1": Location("Lift 1", 6, 5, 1, "lift"),
        "Stairs 1": Location("Stairs 1", 1, 6, 1, "stairs"),
        "Hall C": Location("Hall C", 4, 4, 2, "corridor"),
        "ICU": Location("ICU", 8, 3, 2, "critical"),
        "Operation Theatre": Location("Operation Theatre", 7, 6, 2, "critical"),
        "Ward 201": Location("Ward 201", 2, 2, 2, "ward"),
        "Lift 2": Location("Lift 2", 6, 5, 2, "lift"),
        "Stairs 2": Location("Stairs 2", 1, 6, 2, "stairs"),
    }


def _build_edges(locations: Dict[str, Location]) -> List[Tuple[str, str, float]]:
    links = [
        ("Entrance", "Reception"),
        ("Reception", "Emergency"),
        ("Reception", "Hall A"),
        ("Emergency", "Pharmacy"),
        ("Hall A", "Pharmacy"),
        ("Hall A", "Lift G"),
        ("Hall A", "Stairs G"),
        ("Ward 101", "Hall B"),
        ("Hall B", "Radiology"),
        ("Hall B", "Lab"),
        ("Hall B", "Lift 1"),
        ("Hall B", "Stairs 1"),
        ("Ward 201", "Hall C"),
        ("Hall C", "ICU"),
        ("Hall C", "Operation Theatre"),
        ("Hall C", "Lift 2"),
        ("Hall C", "Stairs 2"),
        ("Lift G", "Lift 1"),
        ("Lift 1", "Lift 2"),
        ("Stairs G", "Stairs 1"),
        ("Stairs 1", "Stairs 2"),
    ]

    edges: List[Tuple[str, str, float]] = []
    for source, destination in links:
        edges.append((source, destination, euclidean_distance(locations[source], locations[destination])))
    return edges


def build_hospital_graph() -> tuple[nx.Graph, Dict[str, Location], List[Tuple[str, str, float]]]:
    """Return the sample hospital graph and its coordinate metadata."""
    locations = _build_locations()
    edges = _build_edges(locations)

    graph = nx.Graph()
    for name, location in locations.items():
        graph.add_node(
            name,
            pos=location.vector,
            floor=location.z,
            category=location.category,
        )

    for source, destination, weight in edges:
        graph.add_edge(source, destination, weight=weight)

    return graph, locations, edges
