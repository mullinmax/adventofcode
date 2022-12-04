with open('data.txt') as f:
    #read data from the file and store it in a list
    data = f.read().split('\n')
    #declare variable for the sum of priorities
    priority_sum = 0
    #loop through the data
    for rucksack in data:
        #declare variables for the first and second compartments
        first_compartment = rucksack[:len(rucksack)//2]
        second_compartment = rucksack[len(rucksack)//2:]
        #find the item that appears in both compartments
        common_item = ''
        for item in first_compartment:
            if item in second_compartment and item not in common_item:
                common_item += item
        #calculate the priority of the item
        priority = 0
        if common_item.islower():
            priority = ord(common_item) - 96
        elif common_item.isupper():
            priority = ord(common_item) - 64 + 26
        #add the priority to the priority sum
        priority_sum += priority
    #print the solution
    print(priority_sum)