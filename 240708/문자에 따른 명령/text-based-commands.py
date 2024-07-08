def calculate_positions(commands):
    x, y, direction = 0, 0, 0  # Starting at origin facing north
    positions = [(x, y, direction)]
    
    # Directions: 0 = North, 1 = East, 2 = South, 3 = West
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

def different_positions(command_string):
    n = len(command_string)
    unique_positions = set()
    
    # Precompute positions for the original command sequence
    positions = calculate_positions(command_string)

    # Directions: 0 = North, 1 = East, 2 = South, 3 = West
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

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