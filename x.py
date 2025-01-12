
class Piece:
    def __init__(self):
        self.tdict = {0: 'X', 1: 'O'}
        self.turn = 0  # start with player X, i.e., player 0
        self.type = self.tdict[self.turn]

    def update_type(self):
        self.type = self.tdict[self.turn]

    def incr_turn(self):
        self.turn = (self.turn + 1) % 2
        self.update_type()


class Board:
    def __init__(self):
        board = []
        for _ in range(3):
            board.append([' ', ' ', ' '])
        self.board = board

    def display(self):
        for row in self.board:
            print(row[0] + '|' + row[1] + '|' + row[2])
            print('-' * 5)

    def place_piece(self, row: int, col: int, p: Piece):
        success = False
        if ((row < 1 or row > 3) or \
           (col < 1 or col > 3) or \
           self.board[row - 1][col - 1] != ' '):
        
            print("Invalid position.")
            return success
        else:
            self.board[row - 1][col - 1] = p.type
            p.incr_turn()
            success = True
            return success

    def check_winner(self):
        for row in self.board: # check horizontal wins
            if (row[0] == row[1] == row[2]) and (row[0] != ' '):
                return row[0]

        for col in range(1, 3): # check vertical wins
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # check diags
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

def ttt():
    player = Piece()
    game = Board()

    while (game.check_winner() is None) and (game.is_full() == False):
        game.display()

        row = int(input(f"Placing {player.type}, Row: "))
        col = int(input(f"Placing {player.type}, Column: "))

        if game.place_piece(row, col, player):
            winner = game.check_winner()
            if winner is not None:
                game.display()
                print(f"Player {winner} wins!")
                break
            elif game.is_full():
                game.display()
                print("It's a tie!")
                break

ttt()
