
import sys
with open(sys.argv[1]) as f:
  instructions = f.readlines()
 
# Create an empty array to store each instruction and its value
instructions_and_values = []

# Iterate through the array of strings and split each instruction into its command and value
for instruction in instructions:
  command_and_value = instruction.split()
  instructions_and_values.append(command_and_value)

# Create a variable to keep track of the cycles and set it to 0
cycles = 0

# Create a variable to store the value of X register and set it to 1
x_register = 1
x_register_history = []
# Iterate through the array of commands and values and: 
signal_strengths = []
for instruction in instructions_and_values:

  # If command is 'noop', increment the cycles variable by 1
  if instruction[0] == 'noop':
    cycles += 1   
    signal_strength = cycles * x_register
    signal_strengths.append(signal_strength)
    x_register_history.append(x_register)
  # If command is 'add', increment the cycles variable by 2 and add the value to X register
  elif instruction[0] == 'addx':
    cycles += 1
    signal_strength = cycles * x_register
    signal_strengths.append(signal_strength)
    x_register_history.append(x_register)
    cycles += 1
    signal_strength = cycles * x_register
    signal_strengths.append(signal_strength)
    x_register_history.append(x_register)
    x_register += int(instruction[1])


# Calculate the sum of the signal strengths stored in the separate array and print it out.
# print(sum(signal_strengths))


for row in range(6):
  for col in range(40):
    if -1 <= x_register_history[row*40+col] - col <= 1:
      print('#', end='')
    else:
      print('.', end='')
  print()