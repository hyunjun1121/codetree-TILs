def calculate_positions(commands):
    x, y, direction = 0, 0, 0
    positions = [(x, y, direction)]
    
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
    
    positions = calculate_positions(command_string)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(n):
        x, y, direction = positions[i]
        
        for new_command in ['L', 'R', 'F']:
            if command_string[i] != new_command:
                new_x, new_y, new_direction = x, y, direction
                
                if new_command == 'L':
                    new_direction = (new_direction - 1) % 4
                elif new_command == 'R':
                    new_direction = (new_direction + 1) % 4
                elif new_command == 'F':
                    new_x += dx[new_direction]
                    new_y += dy[new_direction]
                
                for j in range(i + 1, n):
                    command = command_string[j]
                    if command == 'L':
                        new_direction = (new_direction - 1) % 4
                    elif command == 'R':
                        new_direction = (new_direction + 1) % 4
                    elif command == 'F':
                        new_x += dx[new_direction]
                        new_y += dy[new_direction]
                
                unique_positions.add((new_x, new_y))
    
    return len(unique_positions)

# Example usage
command_string = input().strip()
print(different_positions(command_string))