import chess
import chess.svg
from negamax import negamax
from eval import getEval
from negascout import negascout
from PVS import PVS
import sys, getopt

board = chess.Board()

INFINITY = 999999


def calculateBestMove(depth, board, searchfunc):
    legalMoves = board.legal_moves
    bestMove = None

    maxScore = -INFINITY

    for move in legalMoves:
        board.push(move)

        if searchfunc == 'negamax':
            score = negamax(depth - 1, board)
        elif searchfunc == 'negascout':
            score = negascout(depth - 1, board, -INFINITY, INFINITY)
        elif searchfunc == 'PVS':
            score = PVS(depth - 1, board, -INFINITY, INFINITY)
        print(board)
        board.pop()
        if score >= maxScore:
            print('New good move! ' + str(move.uci()) + ' with score of ' + str(score))
            maxScore = score
            bestMove = move
    return bestMove

def main(argv):
    board = chess.Board()
    opts, args = getopt.getopt(argv,"s:",["searchfunc="])
    searchfunc = 'negamax'
    for opt, arg in opts:
        if opt in ("-s", "--searchfunc"):
            searchfunc = arg

    while 1:
        cpuMove = calculateBestMove(1, board, searchfunc)
        print('CPU played ' + board.san(cpuMove))
        board.push(cpuMove)
        print(board)
        svg = chess.svg.board(board)
        with open('board.svg', 'w') as file:
            file.write(svg)

        move = input("Enter a move:")
        if str(move) == 'score':
            print('Current score: ' + str(getEval(board)))
            move = input("Enter a move:")
        board.push_san(str(move))

if __name__ == "__main__":
   main(sys.argv[1:])