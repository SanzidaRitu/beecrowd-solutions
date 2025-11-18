from typing import List, Tuple

def compute_horror_index(graph: List[List[int]], horror_list: List[int]) -> List[int]:
    horror_index = [float("inf") for i in range(len(graph))]

    queue = []

    for movie in horror_list:
        horror_index[movie] = 0
        queue.append(movie)

    while queue:
        movie = queue.pop(0)
        for neighbor in graph[movie]:
            if horror_index[neighbor] == float("inf"):
                horror_index[neighbor] = horror_index[movie] + 1
                queue.append(neighbor)

    return horror_index

def find_best_movie(N: int, H: int, L: int, horror_list: List[int], similarities: List[Tuple[int, int]]) -> int:
    graph = [[] for i in range(N)]
    for a, b in similarities:
        graph[a].append(b)
        graph[b].append(a)

    horror_index = compute_horror_index(graph, horror_list)

    best_movie = 0
    best_horror_index = 0
    for movie in range(N):
        if horror_index[movie] > best_horror_index:
            best_horror_index = horror_index[movie]
            best_movie = movie

    return best_movie

N, H, L = map(int, input().split())
horror_list = list(map(int, input().split()))
similarities = [tuple(map(int, input().split())) for i in range(L)]

best_movie = find_best_movie(N, H, L, horror_list, similarities)

print(best_movie)