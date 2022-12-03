with open('data.txt') as f:
    # open data.txt
    data = f.read()
    # read data from file
    data_list = data.split('\n')
    # split data into list 
    h_pos = 0
    # set horizontal position to 0
    d_pos = 0
    # set depth position to 0
    for command in data_list:
        # iterate through commands in list
        cmd_list = command.split(' ')
        # split command into list 
        if cmd_list[0] == 'forward':
            # check if command is 'forward'
            h_pos += int(cmd_list[1])
            # increase horizontal position by value of command 
        elif cmd_list[0] == 'down':
            # check if command is 'down' 
            d_pos += int(cmd_list[1])
            # increase depth position by value of command 
        elif cmd_list[0] == 'up':
            # check if command is 'up' 
            d_pos -= int(cmd_list[1])
            # decrease depth position by value of command 
    
print(h_pos * d_pos)
# multiply horizontal and depth positions to get solution