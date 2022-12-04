with open('data.txt') as f:
  data = [''.join(set(l.strip())) for l in f.readlines()]

# Create an empty dictionary
items = {}

# Once all groups have been processed, iterate through the dictionary
total_sum = 0

priorities = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]
# Iterate through each group of three lines
for i in range(0, len(data), 3):
   group = data[i:i+3]
   # For each group, iterate through the items
   items = {}
   for item in ''.join(group):
      # If the item is already in the dictionary, increase the count by one
      if item in items:
         items[item] += 1
      # Else, add the item to the dictionary with a count of one
      else:
         items[item] = 1

   for item, count in items.items():
   # For each item, check if the count is three
      if count == 3:
         # Add the priority to a total sum
         print(item, priorities.index(item)+1)
         total_sum += priorities.index(item)+1
         break

# Output the total sum
print(total_sum)