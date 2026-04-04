import math
import os

def heuristic(x, y, Dx, Dy):
    return math.sqrt((x - Dx)**2 + (y - Dy)**2)

def get_neighbors(x, y, grid, N):
    directions = [
        (-1,0),(1,0),(0,-1),(0,1),
        (-1,-1),(-1,1),(1,-1),(1,1)
    ]

    neighbors = []

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy 

        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != -1:
            neighbors.append((nx, ny))

    return neighbors

def find_lowest_f(open_list):
    best_index = 0

    for i in range(len(open_list)):
        if open_list[i][0] < open_list[best_index][0]:
            best_index = i

    return best_index

def reconstruct_path(parent, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

def a_star(grid, sx, sy, dx, dy):
    N = len(grid)

    open_list = []
    g_cost = {(sx, sy): 0}
    parent = {(sx, sy): None}
    visited = set()

    f_start = heuristic(sx, sy, dx, dy)
    open_list.append((f_start, 0, sx, sy))

    while open_list:

        idx = find_lowest_f(open_list)
        f, g, x, y = open_list.pop(idx)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == (dx, dy):
            return g, reconstruct_path(parent, (dx, dy))

        for nx, ny in get_neighbors(x, y, grid, N):

            if (nx, ny) in visited:
                continue

            new_g = g + grid[nx][ny]

            if (nx, ny) not in g_cost or new_g < g_cost[(nx, ny)]:
                g_cost[(nx, ny)] = new_g
                parent[(nx, ny)] = (x, y)

                f_new = new_g + heuristic(nx, ny, dx, dy)
                open_list.append((f_new, new_g, nx, ny))

    return None, []

def print_result(cost, path):
    if cost is None:
        print("Optimal Cost: None")
        print("Optimal Path: []")
    else:
        print(f"Optimal Cost: {cost}")

        path_str = ""
        for i in range(len(path)):
            if i == 0:
                path_str += f"({path[i][0]},{path[i][1]})"
            else:
                path_str += f"→({path[i][0]},{path[i][1]})"

        print("Optimal Path:")
        print(path_str)

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    N = int(lines[0])
    grid = [list(map(int, lines[i+1].split())) for i in range(N)]
    Sx, Sy = map(int, lines[N+1].split())
    Dx, Dy = map(int, lines[N+2].split())

    return grid, Sx, Sy, Dx, Dy

def write_output(filename, title, cost, path):
    with open(filename, 'a') as f:
        f.write(" " + title + " \n")
        f.write("Optimal Cost: " + str(cost) + "\n")

        if path:
            f.write("Optimal Path:\n")
            for i in range(len(path)):
                f.write(f"({path[i][0]},{path[i][1]})")
                if i != len(path) - 1:
                    f.write(" -> ")
            f.write("\n\n")
        else:
            f.write("Optimal Path: []\n\n")

if __name__ == "__main__":

    open("output.txt", "w").close()

    # -------- Sample Input 1 --------
    grid1 = [
        [1,1,1,-1],
        [1,-1,1,1],
        [1,1,1,1],
        [1,-1,1,1]
    ]

    sx, sy = 0, 0
    dx, dy = 3, 3

    cost1, path1 = a_star(grid1, sx, sy, dx, dy)
    print("Sample Input 1:")
    print_result(cost1, path1)
    write_output("output.txt", "Sample 1", cost1, path1)

    # -------- Sample Input 2 --------
    grid2 = [
        [2,3,1,-1],
        [1,-1,4,2],
        [1,2,3,1],
        [3,-1,2,1]
    ]

    sx, sy = 0, 0
    dx, dy = 3, 3

    cost2, path2 = a_star(grid2, sx, sy, dx, dy)
    print("\nSample Input 2:")
    print_result(cost2, path2)
    write_output("output.txt", "Sample 2", cost2, path2)

    # -------- Sample Input 3 --------
    grid3 = [
        [ 2, -1,  3],
        [-1, -1, -1],
        [ 3, -1,  2]
    ]

    sx, sy = 0, 0
    dx, dy = 2, 2

    cost3, path3 = a_star(grid3, sx, sy, dx, dy)
    print("\nSample Input 3:")
    print_result(cost3, path3)
    write_output("output.txt", "Sample 3", cost3, path3)

    # -------- File Input --------
    if os.path.exists("input.txt"):
        grid, sx, sy, dx, dy = read_input("input.txt")

        cost, path = a_star(grid, sx, sy, dx, dy)

        print("\nFile Input:")
        print_result(cost, path)

        write_output("output.txt", "File Input", cost, path)