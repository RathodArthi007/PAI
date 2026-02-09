import heapq

GOAL = [['1','2','3'],
        ['4','5','6'],
        ['7','8','e']]

def board_to_string(board):
    return '\n'.join(['-'.join(row) for row in board])

def string_to_board(s):
    return [row.split('-') for row in s.split('\n')]

def find_pos(board, tile):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == tile:
                return i, j

def heuristic(board):
    dist = 0
    for tile in '12345678e':
        r1, c1 = find_pos(board, tile)
        r2, c2 = find_pos(GOAL, tile)
        dist += abs(r1 - r2) + abs(c1 - c2)
    return dist

def neighbors(board):
    r, c = find_pos(board, 'e')
    neighbor_states = []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_board = [row[:] for row in board]
            new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
            neighbor_states.append((new_board, new_board[nr][nc]))
    return neighbor_states

def a_star(initial_board):
    start = board_to_string(initial_board)
    goal = board_to_string(GOAL)
    open_set = []
    heapq.heappush(open_set, (heuristic(initial_board), 0, start, None))
    came_from = {}
    g_score = {start:0}

    while open_set:
        f, g, current, action = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current is not None:
                path.append((came_from.get(current, (None, None))[1], current))
                current = came_from.get(current, (None, None))[0]
            return path[::-1]

        current_board = string_to_board(current)
        for neighbor_board, moved_tile in neighbors(current_board):
            neighbor_str = board_to_string(neighbor_board)
            tentative_g = g + 1
            if tentative_g < g_score.get(neighbor_str, float('inf')):
                g_score[neighbor_str] = tentative_g
                f_score = tentative_g + heuristic(neighbor_board)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor_str, moved_tile))
                came_from[neighbor_str] = (current, moved_tile)

    return None

INITIAL = [['1','e','2'],
           ['6','3','4'],
           ['7','5','8']]

result_path = a_star(INITIAL)

print("Initial configuration")
print(board_to_string(INITIAL))

for i, (move, state) in enumerate(result_path):
    if move is None:
        continue
    print()
    print(f"After moving {move} into the empty space")
    print(state)
