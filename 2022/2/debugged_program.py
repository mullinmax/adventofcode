with open('data.txt') as f:
    # opening the file with the data
    data = f.readlines()
    # creating a variable that stores the data in lines
    total_score = 0
    # setting the initial total score to 0
    for line in data:
        # looping through each line in the data
        line = line.strip().split(' ')
        # stripping each line and splitting it into two elements
        opponent = line[0]
        # setting a variable for the opponent's play 
        player = line[1]
        # setting a variable for the player's play
        if opponent == 'A':
            # if opponent plays rock
            if player == 'Y':
                # and player plays paper 
                total_score += 8
                # add 8 to total score
            elif player == 'X':
                # and player plays rock
                total_score += 4
                # add 1 to total score
            else:
                # and player plays scissors
                total_score += 3
                # add 6 to total score
        elif opponent == 'B':
            # if opponent plays paper 
            if player == 'X':
                # and player plays rock 
                total_score += 1
                # add 8 to total score 
            elif player == 'Y':
                # and player plays paper 
                total_score += 5
                # add 1 to total score 
            else:
                # and player plays scissors 
                total_score += 9
                # add 6 to total score 
        else: 
            # if opponent plays scissors 
            if player == 'Z':
                # and player plays scissors 
                total_score += 6
                # add 8 to total score 
            elif player == 'X':
                # and player plays rock 
                total_score += 7
                # add 1 to total score 
            else: 
                # and player plays paper 
                total_score += 2
                # add 6 to total score 

    print(total_score)
    # printing out the total score