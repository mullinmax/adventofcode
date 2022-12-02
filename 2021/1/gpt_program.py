with open('data.txt') as f:
  # create an empty list
  data_list = []
  # loop through each line in the file
  for line in f:
    # append each line to the list
    data_list.append(int(line))

# create a variable to store the number of measurements larger than the previous one
count = 0
# loop through the list of measurements
for i in range(1, len(data_list)):
  # compare the current measurement to the previous one
  if data_list[i] > data_list[i-1]:
    # increment the counter if the current measurement is larger than the previous one
    count += 1
# print out the solution
print(count)