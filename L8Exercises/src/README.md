How to use:

For CLI version of the Tic Tac Toe game you must create an instance of the TicTacToe class:
    - game = TicTacToe()
By default you play agains the machine and the order of play will change on every consecutive game
you play against the machine.

The second step to play the game is call the newGame() method, which will create the new board and
the game.
    - game.newGame()

You can see the board at any moment in time, but if you use the play() function, it will automatically
show it to you on the screen, as well as the instruction to play the game.
    -game.display()
    -game.play()


Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
game.py                11      3    73%   11, 15, 17
test_ticTacToe.py     248      0   100%
tic_tac_toe.py        188     47    75%   17, 55-82, 101, 104, 121-139, 218, 235-239
-------------------------------------------------
TOTAL                 447     50    89%
