For start the game: 

Run "python app.py"

After the app is run, go to Chrome tab and enter http://127.0.0.1:5000
You will see simple UI for the game.

For play the game:

Press on "Create Game" button.
You will see a unique id for the created game. 
Copy the id and paste it into the blank line and press "Join Game"

Open a new chrome tab and enter http://127.0.0.1:5000
Copy the game id from the last tab into the blank line and press "Join Game"

Now the first player (X) should make his first move, and the second player (O) should play next.
When one of the players hit the goal of 3 in a row, pop-up message will appear for both players.

###############################################################################

Explain for the Code.

Game structured:
I used a socket communication between the server to the clients. 
On creation of a game the BE opens a room for the client and the second player can join this room with an ID.

The game structured, is as simple as it can be. 
The game is an array of 9 empty string that will replaced with X or O on the moves.
Each game has a unique ID, list of two players, turn state and a winner state.


Entities:

###Game###
array of 9 empty string 
unique ID
List of two players
Turn state (set to X)
winner state (set to none).

###Player###
Symbol can be set to 'O' or 'X'.

Flow:
The flow of the game goes like that.
1. First player creates a game and gets an unique ID
2. First player join the game with the received ID
3. Second player join the game with the same ID
4. First player make his move
5. BE checks if it's a legal move. if it is, it sets the move for the player and check the winning condition.
6. If the winner state has a value, we alert the UI on both sides for a winning.
 

Win condition:
Instead of checking each move for all the winning options, I wrote all the winning options in array, because we have a limit winning options.
So, on each move that player does, we check if the player sets the game array with one of the winning options.

winning_options = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
