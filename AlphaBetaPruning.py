def minimax(board, maximizing_player, alpha, beta):
    if board.is_game_over():
        if board.is_winner('X'):
            return -1
        elif board.is_winner('O'):
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = float('-inf')

        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, False, alpha, beta)
            board.undo_move(move)

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float('inf')

        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, True, alpha, beta)
            board.undo_move(move)

            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return min_eval


def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in board.get_available_moves():
        board.make_move(move)
        eval = minimax(board, False, alpha, beta)
        board.undo_move(move)

        if eval > best_eval:
            best_eval = eval
            best_move = move

        alpha = max(alpha, eval)

    return best_move