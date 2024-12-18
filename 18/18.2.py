import re
import heapq
size = 70
start = [0,0]
end = [size,size]
data = []
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#boring pathfinding stuff
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
        return None
    open_list = []
    closed_list = set()
    g_costs = {start: 0}
    f_costs = {start: manhattan_distance(start, end)}
    came_from = {}
    heapq.heappush(open_list, (f_costs[start], start))
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        closed_list.add(current)
        for direction in DIRECTIONS:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1 or neighbor in closed_list:
                    continue
                tentative_g_cost = g_costs[current] + 1
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_costs[neighbor] = tentative_g_cost + manhattan_distance(neighbor, end)
                    came_from[neighbor] = current
                    heapq.heappush(open_list, (f_costs[neighbor], neighbor))
    return None


with open('input.txt') as input:
    lines = input.readlines()
    for line in lines:
        data.append(re.findall(r'[\d]+',line))
    for coordinates in range(len(data)):
        data[coordinates][0] = int(data[coordinates][0])
        data[coordinates][1] = int(data[coordinates][1])

    for bytes in range(0,len(data)-1):
        newData = data[:bytes]
        grid = []
        for Y in range(0,size+1):
            grid.append([])
            for X in range(0,size+1):
                if [X,Y] in newData:
                    grid[-1].append(1)
                else:
                    grid[-1].append(0)
        start = (0,0)
        end = (size,size)
        path = a_star(grid,start,end)
        if path:
            print(path)
            print(len(path))
        else:
            print(data[bytes])
            break

        
    
