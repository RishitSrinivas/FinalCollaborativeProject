import sys

#define all functions:

class Gameboard():

    def __init__(self):
        self.gameboard = {1:' ' , 2: ' ', 3: ' ', 4:' ',  5:' ',  6:' ',  7:' ',  8:' ',  9:' '}

    def setPeice(self, user, position, gameboard):
        gameboard[position] = user
        return gameboard

    @property
    def gameBoard(self):
        return self.gameboard

    def clearboard(self):
        self.gameboard = {1:' ', 2:' ', 3:' ', 4:' ',5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

    def is_place_taken(self, gameboard, index):
        if gameboard[index] != ' ':
            return True

    def is_board_full(self, gameboard):
        for index in range(1, 10):
            if gameboard[index] == ' ':
                return False
        return True

    def is_game_won(self, gameboard):
        win_conds = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        for win_cond in win_conds:
            if gameboard[win_cond[0]] == gameboard[win_cond[1]] and gameboard[win_cond[1]] == gameboard[win_cond[2]] and gameboard[win_cond[0]]!= ' ':
                return True

    def printBoard(self, gameboard):
        index = 0
        for row in range(1, 4):
            for column in range(1, 4):
                index += 1
                if column != 3:
                    print(gameboard[index], end='')
                    print('|', end='')
                else:
                    print(gameboard[index])

class Game():

    def on_start(self):
        self.controlBoard = Gameboard()
        self.gameboard = self.controlBoard.gameboard
        self.playerOne = 'x'
        self.playerTwo = 'o'
        print("Let's start playing Tic-Tac-Toe.")
        print("What is player one's name?")
        self.player_one = input(' : ')
        print("What is player two's name?")
        self.player_two = input(' : ')
        print('Each place in the gameboard are represented by 1-9, starting from left column each time moving along the row.')
        self.controlBoard.printBoard(self.gameboard)
        self.turn = 1

    def on_end(self):
        #Checks if a player wants to end the game.
        if self.running == False:
            replay = input('Press 0 to quit or 1 to play again: ')
            try:
                if int(replay):
                    if int(replay) == 0:
                        sys.exit()
                    else:
                        if int(replay) == 1:
                            self.running = True
                            self.on_start()
                        else :
                            print("Wrong Value. Press 0 to quit or 1 to play again: ")
                            self.on_end() 

            except:
                print("A number must be entered.")
                self.on_end()

    def takeTurn(self, user, peice):
        print(user + ' choose a place, 1-9')
        try:
            position = int(input(': '))
            if position > 9 or position < 1:
                raise Exception

        except:
            print('Pick a number between 1-9')
            return self.takeTurn(user, peice)

        if self.controlBoard.is_place_taken(self.gameboard, position):
            print("That place is taken.")
            self.takeTurn(user,peice)
        else:
            self.controlBoard.setPeice(peice, position, self.gameboard)
            self.controlBoard.printBoard(self.gameboard)
            if self.controlBoard.is_game_won(self.gameboard):
                print(user +  " wins.")
                self.running = False 

    def main(self):
        self.running = True
        self.on_start()
        while self.running:
            if self.turn%2 != 0:
                self.takeTurn(self.player_one, 'x')
            else:
                self.takeTurn(self.player_two, 'o')

            if self.controlBoard.is_board_full(self.gameboard):
                print("It's a draw!! You both lose!")
                self.running = False
            self.turn += 1

            if not self.running:
                self.on_end()

if __name__ == '__main__':
    Game().main()
