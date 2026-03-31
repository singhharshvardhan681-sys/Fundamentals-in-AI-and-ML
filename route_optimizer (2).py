import json
import heapq

def load_graph(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    graph = {place: [] for place in data['places']}
    for edge in data['edges']:
        graph[edge['from']].append((edge['to'], edge['distance'], edge['time']))
        graph[edge['to']].append((edge['from'], edge['distance'], edge['time']))  # undirected
    return graph

def dijkstra(graph, start, end, weight_index):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return cost, path
        for neighbor, distance, time in graph[node]:
            weight = distance if weight_index == 0 else time
            heapq.heappush(queue, (cost + weight, neighbor, path))
    return float('inf'), []

def main():
    graph = load_graph('sample_graph.json')
    print('Places:', ', '.join(graph.keys()))
    start = input('Enter start location: ').strip()
    end = input('Enter end location: ').strip()
    if start not in graph or end not in graph:
        print('Invalid locations. Please try again.')
        return
    print('Choose optimization:')
    print('1. Shortest Distance')
    print('2. Shortest Time')
    choice = input('Enter 1 or 2: ').strip()
    if choice == '1':
        cost, path = dijkstra(graph, start, end, 0)
        print(f'Shortest distance: {cost}')
    elif choice == '2':
        cost, path = dijkstra(graph, start, end, 1)
        print(f'Shortest time: {cost}')
    else:
        print('Invalid choice.')
        return
    print('Route:', ' -> '.join(path))

if __name__ == '__main__':
    main()
