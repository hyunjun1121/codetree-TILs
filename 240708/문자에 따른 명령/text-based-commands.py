def different_positions(command_string):
    n = len(command_string)
    unique_positions = set()
    
    # Direction vectors (north, east, south, west)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # Precompute the position and direction after each command
    x, y, direction = 0, 0, 0
    positions = [(x, y, direction)]
    
    for command in command_string:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            x += dx[direction]
            y += dy[direction]
        positions.append((x, y, direction))
    
    # For each command, modify it and calculate the resulting position
    for i in range(n):
        for new_command in ['L', 'R', 'F']:
            if command_string[i] != new_command:
                # Get the state before the modified command
                x, y, direction = positions[i]
                
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