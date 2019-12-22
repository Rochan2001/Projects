class Tictactoe:
    board = ['_ ', '_ ', '_ ',
             '_ ', '_ ', '_ ',
             '_ ', '_ ', '_ ']

    def display_board(self):
        pass

    def check_win(self):
        pass

    def check_tie(self):
        pass


class Display(Tictactoe):
    def __init__(self):
        pass

    def display_board(self):
        print("\n", Tictactoe.board[0], '|', Tictactoe.board[1], '|', Tictactoe.board[2], "     1 | 2 | 3", '\n',
              Tictactoe.board[3], '|', Tictactoe.board[4], '|', Tictactoe.board[5], "     4 | 5 | 6", '\n',
              Tictactoe.board[6], '|', Tictactoe.board[7], '|', Tictactoe.board[8], "     7 | 8 | 9", '\n')


class Game(Display, Tictactoe):
    def check_win(self):
        count = 0
        for i in range(3):
            count = 0
            count1 = 0
            for j in range(i, 9, 3):
                if Tictactoe.board[j] == 'X ':
                    count += 1
                elif Tictactoe.board[j] == 'O ':
                    count1 += 1
            if count == 3 or count1 == 3:
                return True
                break
        for i in range(0, 7, 3):
            count = 0
            count1 = 0
            for j in range(i, i + 3):
                if Tictactoe.board[j] == 'X ':
                    count += 1
                elif Tictactoe.board[j] == 'O ':
                    count1 += 1
            if count == 3 or count1 == 3:
                return True
                break
        if (Tictactoe.board[0] == 'X ' and Tictactoe.board[4] == 'X ' and Tictactoe.board[8] == 'X ') or (
                Tictactoe.board[0] == 'O ' and Tictactoe.board[4] == 'O ' and Tictactoe.board[8] == 'O '):
            return True
        if (Tictactoe.board[2] == 'X ' and Tictactoe.board[4] == 'X ' and Tictactoe.board[6] == 'X ') or (
                Tictactoe.board[2] == 'O ' and Tictactoe.board[4] == 'O ' and Tictactoe.board[6] == 'O '):
            return True

    def check_tie(self):
        count = 0
        count1 = 0
        for i in range(9):
            if Tictactoe.board[i] == 'X ':
                count += 1
            elif Tictactoe.board[i] == 'O ':
                count1 += 1
        if count + count1 == 9:
            return True
        else:
            return False

    def play_game(self):
        print("Player 1 is X and player 2 is O")
        while (1):
            rochan = 0
            while (rochan < 1):
                Display.display_board(Display)
                rochan += 1
            print("X's Turn")
            while (1):
                pos = int(input('Choose a position from 1-9: '))
                if Tictactoe.board[pos - 1] == "_ ":
                    Tictactoe.board[pos - 1] = 'X '
                    break
                else:
                    print("Occupied please enter another position")
            Display.display_board(Display)
            win = Game.check_win(Game)
            if win:
                print("X won the game!!!")
                break
            tie = Game.check_tie(Game)
            if tie:
                print("DRAW!!!")
                break
            print("O's Turn")
            while (1):
                pos = int(input('Choose a position from 1-9: '))
                if Tictactoe.board[pos - 1] == "_ ":
                    Tictactoe.board[pos - 1] = 'O '
                    break
                else:
                    print("Occupied please enter another position")
            Display.display_board(Display)
            win = Game.check_win(Game)
            if win:
                print("O won the game!!!")
                break
            tie = Game.check_tie(Game)
            if tie:
                print("DRAW!!!")
                break


g = Game()
g.play_game()
