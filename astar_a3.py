def a_star_grid(grid, start, goal):
    from queue import PriorityQueue
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    pq = PriorityQueue()
    pq.put((0, 0, start, [start]))
    visited = set()

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while not pq.empty():
        f, g, current, path = pq.get()
        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            nx, ny = current[0]+dx, current[1]+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] != '#':
                neighbor = (nx, ny)
                cost = 1 if grid[nx][ny] == '.' else 2
                new_g = g + cost
                new_f = new_g + heuristic(neighbor, goal)
                pq.put((new_f, new_g, neighbor, path + [neighbor]))
    return None

# Contoh penggunaan untuk pengiriman makanan
food_map = [
    ['R', '.', '.', '#', 'C'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.']
]

start = (0, 0)
goal = (0, 4)
print("Food Delivery A* Path:", a_star_grid(food_map, start, goal))
