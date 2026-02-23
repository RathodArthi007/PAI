# Tic Tac Toe using Alphabets (A-I)

board = [' '] * 9

positions = {
    'A':0, 'B':1, 'C':2,
    'D':3, 'E':4, 'F':5,
    'G':6, 'H':7, 'I':8
}

wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def show():
    print("\nCurrent Board:")
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def winner(p):
    return any(board[a]==board[b]==board[c]==p for a,b,c in wins)

def full():
    return ' ' not in board

def minimax(is_max):
    if winner('O'): return 1
    if winner('X'): return -1
    if full(): return 0

    best = -100 if is_max else 100

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if is_max else 'X'
            score = minimax(not is_max)
            board[i] = ' '
            best = max(best, score) if is_max else min(best, score)

    return best

def best_move():
    best_score = -100
    move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


# =====================
# GAME LOOP
# =====================

print("Board Positions:")
print("A|B|C")
print("-----")
print("D|E|F")
print("-----")
print("G|H|I")

while True:
    show()

    # User Turn
    move = input("Enter position (A-I): ").upper()

    if move not in positions:
        print("Invalid input! Use A-I.")
        continue

    index = positions[move]

    if board[index] != ' ':
        print("Position already taken!")
        continue

    board[index] = 'X'

    if winner('X'):
        show()
        print("You win!")
        break

    if full():
        show()
        print("It's a draw!")
        break

    # AI Turn
    print("AI (O) is thinking...")
    ai = best_move()
    board[ai] = 'O'
    print("AI played.")

    if winner('O'):
        show()
        print("You lose!")
        break

    if full():
        show()
        print("It's a draw!")
        break
