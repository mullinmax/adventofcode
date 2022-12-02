with open('data.txt') as f:
  # Open the file and assign the contents to a variable
  data = f.readlines()

# Create a variable to store the total score
total_score = 0

# Loop through each line in the data
for line in data:
  # Split the line into two elements, the opponent's choice and our choice
  opponent_choice, our_choice = line.strip().split()

  # Create a variable to store the score for the round
  round_score = 0

  # Assign a number to each choice (rock = 1, paper = 2, scissors = 3)
  if opponent_choice == 'A':
    opponent_choice_num = 1
  elif opponent_choice == 'B':
    opponent_choice_num = 2
  else:
    opponent_choice_num = 3

  if our_choice == 'X':
    our_choice_num = 1
  elif our_choice == 'Y':
    our_choice_num = 2
  else:
    our_choice_num = 3

  # Calculate the round score based on our choice and the outcome of the round
  if our_choice_num == opponent_choice_num:
    # If it's a draw, add 3 to the round score
    round_score += 3
  elif our_choice_num > opponent_choice_num:
    # If we win, add 6 to the round score
    round_score += 6
  elif our_choice_num < opponent_choice_num:
    # If we lose, add 0 to the round score
    round_score += 0

  # Add the score for our choice to the round score
  round_score += our_choice_num

  # Add the round score to the total score
  total_score += round_score

# Print out the total score
print(total_score)