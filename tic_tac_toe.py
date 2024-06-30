class TicTacToe:
    # Initialize the TicTacToe board and set the starting player.
    def __init__(self):
        self.ttt = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' ',
        }
        self.current_player = 'X'

    # Print the current state of the TicTacToe board.
    def print_tile(self):
        print(self.ttt['top-l'] + ' | ' + self.ttt['top-c'] + ' | ' + self.ttt['top-r'])
        print('--+---+--')
        print(self.ttt['mid-l'] + ' | ' + self.ttt['mid-c'] + ' | ' + self.ttt['mid-r'])
        print('--+---+--')
        print(self.ttt['bot-l'] + ' | ' + self.ttt['bot-c'] + ' | ' + self.ttt['bot-r'])

    # Check if the specified player has won the game.
    def check_winner(self, player):
        win_conditions = [
            ['top-l', 'top-c', 'top-r'],
            ['mid-l', 'mid-c', 'mid-r'],
            ['bot-l', 'bot-c', 'bot-r'],
            ['top-l', 'mid-l', 'bot-l'],
            ['top-c', 'mid-c', 'bot-c'],
            ['top-r', 'mid-r', 'bot-r'],
            ['top-l', 'mid-c', 'bot-r'],
            ['top-r', 'mid-c', 'bot-l']
        ]
        for condition in win_conditions:
            if all(self.ttt[pos] == player for pos in condition):
                return True
        return False

    # Check if the game is a draw (Example: all cells are filled and there is no winner).
    def check_draw(self):
        return all(space != ' ' for space in self.ttt.values())

    # Main game loop that alternates between players and checks for a winner or draw after each move.
    def play_game(self):
        while True:  # maximum of 9 moves
            self.print_tile()
            move = input(f"Turn of {self.current_player}. Move to which space?")
            if self.ttt.get(move) == ' ':
                self.ttt[move] = self.current_player
                print(f"Turn of {self.current_player}. Move to which space? " + move)
            else:
                print("Invalid move, try again.")
                continue
            
            if self.check_winner(self.current_player):
                self.print_tile()
                print(f"Player {self.current_player} wins!")
                break
            
            if self.check_draw():
                self.print_tile()
                print("It's a draw!")
                break
            
            self.current_player = 'O' if self.current_player == 'X' else 'X'
