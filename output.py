with open('data.txt') as f:
    data = f.read()

# Create a list of lines in the file
lines = data.split('\n')

# Initialize total score to 0
total_score = 0

# Iterate through each line in the file
for line in lines:
    # Check if the line is a strategy guide
    if 'A ' in line and 'B ' in line and 'C ' in line:
        # Split the strategy guide into three parts
        part1, part2, part3 = line.split('\n')

        # Extract opponent's choice and player's choice from each part
        opponent_choice1, player_choice1 = part1.split(' ')
        opponent_choice2, player_choice2 = part2.split(' ')
        opponent_choice3, player_choice3 = part3.split(' ')

        # Initialize score for each round to 0
        score1 = 0
        score2 = 0
        score3 = 0

        # Calculate score for round 1
        if opponent_choice1 == 'A': # Opponent chose Rock
            if player_choice1 == 'Y': # Player chose Paper
                score1 = 2 + 6 # 2 for choosing Paper + 6 for winning the round
            elif player_choice1 == 'X': # Player chose Rock
                score1 = 1 + 0 # 1 for choosing Rock + 0 for losing the round
            elif player_choice1 == 'Z': # Player chose Scissors
                score1 = 3 + 0 # 3 for choosing Scissors + 0 for losing the round

        # Calculate score for round 2
        if opponent_choice2 == 'B': # Opponent chose Paper
            if player_choice2 == 'X': # Player chose Rock
                score2 = 1 + 0 # 1 for choosing Rock + 0 for losing the round
            elif player_choice2 == 'Y': # Player chose Paper
                score2 = 2 + 6 # 2 for choosing Paper + 6 for winning the round
            elif player_choice2 == 'Z': # Player chose Scissors
                score2 = 3 + 0 # 3 for choosing Scissors + 0 for losing the round

        # Calculate score for round 3
        if opponent_choice3 == 'C': # Opponent chose Scissors
            if player_choice3 == 'Z': # Player chose Scissors
                score3 = 3 + 3 # 3 for choosing Scissors + 3 for drawing the round
            elif player_choice3 == 'X': # Player chose Rock
                score3 = 1 + 6 # 1 for choosing Rock + 6 for winning the round
            elif player_choice3 == 'Y': # Player chose Paper
                score3 = 2 + 0 # 2 for choosing Paper + 0 for losing the round

        # Add the scores of each round to get the total score 
        total_score += score1 + score2 + score3 

# Print the total score of the tournament 
print('Total Score:', total_score)