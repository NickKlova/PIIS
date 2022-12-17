import chess
from eval import getEval
def negamax(depth, board):
    if depth == 0:
        finalEval = getEval(board)
        return -finalEval
    max = -99999
    legalMoves = board.legal_moves
    for move in legalMoves:
        board.push(move)
        score = -negamax(depth - 1, board)
        board.pop()
        if score > max:
            max = score
    return -max