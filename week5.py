class TicTacToe:

    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i] + "|" + self.board[i+1] + "|" + self.board[i+2])
            if i < 6:
                print("-----")

    def is_winner(self, player):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def get_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, move):
        self.board[move] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'


def minimax(game, is_max):

    if game.is_winner('O'):
        return 1
    if game.is_winner('X'):
        return -1
    if game.is_full():
        return 0

    if is_max:
        best = -100
        for move in game.get_moves():
            game.make_move(move)
            score = minimax(game, False)
            game.undo_move(move)
            best = max(best, score)
        return best
    else:
        best = 100
        for move in game.get_moves():
            game.make_move(move)
            score = minimax(game, True)
            game.undo_move(move)
            best = min(best, score)
        return best


def best_move(game):
    best_score = -100
    move_choice = None

    for move in game.get_moves():
        game.make_move(move)
        score = minimax(game, False)
        game.undo_move(move)

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice


# =======================
# MAIN PROGRAM
# =======================

game = TicTacToe()

while True:

    game.print_board()

    if game.current_player == 'X':
        move = int(input("Enter your move (0-8): "))
        if move not in game.get_moves():
            print("Invalid move!")
            continue
        game.make_move(move)

    else:
        print("AI (O) is thinking...")
        move = best_move(game)
        print("AI plays:", move)
        game.make_move(move)

    if game.is_winner('X'):
        game.print_board()
        print("You win!")
        break

    if game.is_winner('O'):
        game.print_board()
        print("You lose!")
        break

    if game.is_full():
        game.print_board()
        print("It's a draw!")
        break
