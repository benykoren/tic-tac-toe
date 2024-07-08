import uuid


class Game:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.board = [' ' for _ in range(9)]
        self.players = []
        self.current_turn = 'X'
        self.winner = None

    def add_player(self, player):
        if len(self.players) < 2:
            self.players.append(player)
            return True
        return False

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player.symbol
            self.check_winner()
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        winning_options = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_options:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.winner = self.board[combo[0]]
                break


class Player:
    def __init__(self, symbol):
        self.symbol = symbol
