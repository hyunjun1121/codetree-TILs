def get_new_position(commands):
    # Initial position and direction (facing north)
    x, y = 0, 0
    direction = 0 # 0: north, 1: east, 2: south, 3: west

    # Direction vectors for north, east, south, west
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            x += dx[direction]
            y += dy[direction]
    
    return (x, y)

def different_positions(command_string):
    n = len(command_string)
    unique_positions = set()
    
    # Check all possible incorrect commands
    for i in range(n):
        for new_command in ['L', 'R', 'F']:
            if command_string[i] != new_command:
                new_commands = command_string[:i] + new_command + command_string[i+1:]
                final_position = get_new_position(new_commands)
                unique_positions.add(final_position)
    
    return len(unique_positions)

# Example usage:
command_string = input().strip()
print(different_positions(command_string))