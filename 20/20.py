import re
import heapq
data = []
start = (0,0)
end = (0,0)
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
    for line in range(len(lines)):
        data.append([])
        for character in range(len(lines[line])):
            if lines[line][character] == "#":
                data[-1].append(1)
            else:
                data[-1].append(0)
                if lines[line][character] == "S":
                    start = (character,line)
                elif lines[line][character] == "E":
                    end = (character,line)
        
    for line in data:    
        print(line)
    grid = data.copy()
    for a in data:
        if line
    path = a_star(grid,start,end)

    if path:
        for line in range(len(lines)):
            for character in range(len(lines[line])):
                if (character,line) in path:
                    print("O",end="")
                else:
                    print(lines[line][character],end="")


        print(path)
        print(len(path))
    else:
        print("no path")

    
    
