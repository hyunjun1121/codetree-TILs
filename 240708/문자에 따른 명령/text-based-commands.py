def unique_destinations(commands):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def move_and_get_position(commands):
        x, y = 0, 0
        dir_index = 0
        for command in commands:
            if command == 'L':
                dir_index = (dir_index - 1) % 4
            elif command == 'R':
                dir_index = (dir_index + 1) % 4
            elif command == 'F':
                x += directions[dir_index][0]
                y += directions[dir_index][1]
        return (x, y)

    original_position = move_and_get_position(commands)
    unique_positions = set()
    unique_positions.add(original_position)
    
    for i in range(len(commands)):
        modified_commands = list(commands)
        if commands[i] == 'L':
            modified_commands[i] = 'R'
            unique_positions.add(move_and_get_position(modified_commands))
            modified_commands[i] = 'F'
            unique_positions.add(move_and_get_position(modified_commands))
        elif commands[i] == 'R':
            modified_commands[i] = 'L'
            unique_positions.add(move_and_get_position(modified_commands))
            modified_commands[i] = 'F'
            unique_positions.add(move_and_get_position(modified_commands))
        elif commands[i] == 'F':
            modified_commands[i] = 'L'
            unique_positions.add(move_and_get_position(modified_commands))
            modified_commands[i] = 'R'
            unique_positions.add(move_and_get_position(modified_commands))
    
    return len(unique_positions)

# Input and Output
commands = input().strip()
print(unique_destinations(commands))