
import sys
with open(sys.argv[1]) as f:
    data = f.read()

# Create empty list to store last four characters
char_list = []

# Iterate through the data stream buffer
for i, char in enumerate(data):
    # Append each character to the list
    char_list.append(char)
    print(i, char_list)
    # Check if all the characters in the list are different
    if len(set(char_list)) == len(char_list) and i > 13:
        # If all characters are different, return the position of the first character in the list
        print(i)
        break
        
    # If the list contains more than four characters, remove the oldest character
    if len(char_list) > 14:
        char_list.pop(0)