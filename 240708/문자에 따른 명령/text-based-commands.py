def preprocess_positions(commands):
    # Initial position and direction (facing north)
    x, y, direction = 0, 0, 0
    positions = [(x, y, direction)]
    
    # Direction vectors (north, east, south, west)
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
        positions.append((x, y, direction))
    
    return positions

def calculate_final_positions(commands, positions, n):
    unique_positions = set()
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(n):
        for new_command in ['L', 'R', 'F']:
            if commands[i] != new_command:
                x, y, direction = positions[i]
                
                if new_command == 'L':
                    direction = (direction - 1) % 4
                elif new_command == 'R':
                    direction = (direction + 1) % 4
                elif new_command == 'F':
                    x += dx[direction]
                    y += dy[direction]
                
                for j in range(i + 1, n):
                    command = commands[j]
                    if command == 'L':
                        direction = (direction - 1) % 4
                    elif command == 'R':
                        direction = (direction + 1) % 4
                    elif command == 'F':
                        x += dx[direction]
                        y += dy[direction]
                
                unique_positions.add((x, y))
    
    return unique_positions

def different_positions(command_string):
    n = len(command_string)
    positions = preprocess_positions(command_string)
    unique_positions = calculate_final_positions(command_string, positions, n)
    return len(unique_positions)

# Example usage
command_string = input().strip()
print(different_positions(command_string))