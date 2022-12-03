with open('data.txt') as f:#open file
  data = f.readlines() #read each line
  gamma_rate = '' #initialize gamma rate string
  epsilon_rate = '' #initialize epsilon rate string
  for i in range(len(data[0])-1): #loop through each column
    ones = 0 #number of ones
    zeroes = 0 #number of zeroes
    for line in data: #loop through each line
      if line[i] == '1': #if the character is 1, increment ones
        ones += 1
      else: #if the character is 0, increment zeroes
        zeroes += 1
    if ones > zeroes: #if more ones than zeroes, add 1 to gamma rate
      gamma_rate += '1'
    else: #if more zeroes than ones, add 0 to gamma rate
      gamma_rate += '0'
    if ones < zeroes: #if more zeroes than ones, add 1 to epsilon rate
      epsilon_rate += '1'
    else: #if more ones than zeroes, add 0 to epsilon rate
      epsilon_rate += '0'
  gamma_rate = int(gamma_rate,2) #convert gamma rate to int
  epsilon_rate = int(epsilon_rate,2) #convert epsilon rate to int
  power_consumption = gamma_rate * epsilon_rate #calculate power consumption
  print(power_consumption) #print power consumption