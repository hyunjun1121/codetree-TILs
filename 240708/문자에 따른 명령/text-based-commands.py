def calculate_positions(commands):
    # Initialize position and direction (facing North)
    x, y, direction = 0, 0, 0
    n = len(commands)
    
    # Direction vectors (North, East, South, West)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # Prefix positions and directions
    prefix_positions = [(x, y, direction)]
    
    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            x += dx[direction]
            y += dy[direction]
        prefix_positions.append((x, y, direction))
    
    return prefix_positions

def different_positions(command_string):
    n = len(command_string)
    
    # Compute prefix positions
    prefix_positions = calculate_positions(command_string)
    
    # Initialize the set of unique positions
    unique_positions = set()
    
    # Direction vectors (North, East, South, West)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # Simulate correcting each command
    for i in range(n):
        for new_command in ['L', 'R', 'F']:
            if command_string[i] != new_command:
                # Get the state before the modified command
                x, y, direction = prefix_positions[i]
                
                # Apply the modified command
                if new_command == 'L':
                    direction = (direction - 1) % 4
                elif new_command == 'R':
                    direction = (direction + 1) % 4
                elif new_command == 'F':
                    x += dx[direction]
                    y += dy[direction]

                # Continue with the rest of the commands
                for j in range(i + 1, n):
                    command = command_string[j]
                    if command == 'L':
                        direction = (direction - 1) % 4
                    elif command == 'R':
                        direction = (direction + 1) % 4
                    elif command == 'F':
                        x += dx[direction]
                        y += dy[direction]
                
                # Store the resulting position
                unique_positions.add((x, y))
    
    return len(unique_positions)

# Example usage
command_string = input().strip()
print(different_positions(command_string))