"""Run the PathMatrix 3D hospital navigation demo."""

from __future__ import annotations

import argparse
import string

from graph_builder import build_hospital_graph
from floor_mapper import adjacency_matrix
from pathfinder import describe_route, find_shortest_path
from visualization import plot_hospital_route


def normalize_location_name(value: str) -> str:
    cleaned = value.strip().strip(string.punctuation)
    return " ".join(cleaned.lower().split())


def resolve_location(value: str, valid_locations: list[str]) -> str | None:
    normalized_lookup = {
        normalize_location_name(location): location for location in valid_locations
    }
    return normalized_lookup.get(normalize_location_name(value))


def choose_location(prompt: str, valid_locations: list[str]) -> str:
    while True:
        choice = input(prompt).strip()
        resolved = resolve_location(choice, valid_locations)
        if resolved:
            return resolved
        print("\nInvalid location. Choose one of these:")
        print(", ".join(valid_locations))


def choose_algorithm() -> str:
    while True:
        choice = input("Choose algorithm (`dijkstra` or `astar`) [dijkstra]: ").strip().lower()
        if not choice:
            return "dijkstra"
        if choice in {"dijkstra", "astar", "a*"}:
            return "astar" if choice == "a*" else choice
        print("Please enter `dijkstra` or `astar`.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hospital indoor navigation demo.")
    parser.add_argument("--source", help="Starting location")
    parser.add_argument("--destination", help="Destination location")
    parser.add_argument(
        "--algorithm",
        default="dijkstra",
        choices=["dijkstra", "astar"],
        help="Shortest path algorithm to use",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Skip opening the Matplotlib 3D visualization window",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    graph, locations, edges = build_hospital_graph()
    available_locations = sorted(locations.keys(), key=lambda name: (locations[name].z, name))

    print("\nPathMatrix 3D: Hospital Indoor Navigation")
    print("-" * 44)
    print("Available locations:")
    for name in available_locations:
        location = locations[name]
        print(f"- {name} ({location.floor_label}, coordinates=({location.x}, {location.y}, {location.z}))")

    if args.source:
        resolved_source = resolve_location(args.source, available_locations)
        if not resolved_source:
            raise ValueError(f"Unknown source location: {args.source}")
        source = resolved_source
    else:
        source = choose_location("\nEnter source: ", available_locations)

    if args.destination:
        resolved_destination = resolve_location(args.destination, available_locations)
        if not resolved_destination:
            raise ValueError(f"Unknown destination location: {args.destination}")
        destination = resolved_destination
    else:
        destination = choose_location("Enter destination: ", available_locations)

    algorithm = args.algorithm if args.source or args.destination else choose_algorithm()

    path, distance = find_shortest_path(graph, locations, source, destination, algorithm=algorithm)
    steps = describe_route(path, locations)
    matrix = adjacency_matrix(locations, edges)

    print("\nShortest path:")
    print(" -> ".join(path))
    print(f"Total route distance: {distance:.2f} units")

    print("\nStep-by-step guidance:")
    for index, step in enumerate(steps, start=1):
        print(f"{index}. {step}")

    print("\nAdjacency matrix shape:", matrix.shape)
    if args.no_plot:
        print("Visualization skipped because `--no-plot` was provided.")
    else:
        print("Launching 3D visualization...")
        plot_hospital_route(locations, edges, path)


if __name__ == "__main__":
    main()
