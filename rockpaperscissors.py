import random

def game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please enter your move: rock, paper, or scissors")

    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0

    while True:  # The main game loop.
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True:  # The player input loop.
            print('Enter your move: (rock, paper, scissors)')
            playerMove = input()
            if playerMove == 'quit' or playerMove == 'q':
                return
            elif playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissors':
                break  # break out of the player input loop.
            print('Type one of rock, paper, scissors, quit, or q.')

        # Display the player's move.
        print('Player plays: ' + playerMove)
        if playerMove == 'rock':
            print('Rock does not beat paper or scissors.')
        elif playerMove == 'paper':
            print('Paper beats rock.')
        elif playerMove == 'scissors':
            print('Scissors beats paper and rock.')

        # Display what the computer plays.
        randomNumber = random.randint(0, 2)  # 0 represents rock, 1 represents paper, 2 represents scissors
        # Convert the random number into a move.
        if randomNumber == 0:
            computerMove = 'rock'
        elif randomNumber == 1:
            computerMove = 'paper'
        elif randomNumber == 2:
            computerMove = 'scissors'

        print('Computer plays: ' + computerMove)

        # Determine the winner.
        if playerMove == computerMove:
            print('It\'s a tie!')
            ties = ties + 1
        elif (playerMove == 'rock' and computerMove == 'scissors') or \
             (playerMove == 'paper' and computerMove == 'rock') or \
             (playerMove == 'scissors' and computerMove == 'paper'):
            print('You win!')
            wins = wins + 1
        elif (playerMove == 'scissors' and computerMove == 'rock') or \
             (playerMove == 'rock' and computerMove == 'paper') or \
             (playerMove == 'paper' and computerMove == 'scissors'):
            print('You lose!')
            losses = losses + 1

game()
