with open('data.txt') as f:
    instructions = f.read()

# Set the current floor to 0
current_floor = 0

# Loop through the instructions one character at a time
for char in instructions:
    # If the character is an opening parenthesis, increase the current floor by 1
    if char == '(':
        current_floor += 1
    # If the character is a closing parenthesis, decrease the current floor by 1
    elif char == ')':
        current_floor -= 1

# Output the current floor
print(current_floor)