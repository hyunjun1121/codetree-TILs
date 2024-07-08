def get_final_coordinates(commands):
    # Function to simulate movement and return the final coordinates
    direction = 0  # 0: north, 1: east, 2: south, 3: west
    x, y = 0, 0
    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
    return (x, y)

def find_distinct_destinations(commands):
    possible_destinations = set()
    
    for i in range(len(commands)):
        for new_command in "LRF":
            if commands[i] == new_command:
                continue
            
            # Create a new command list with one change
            new_commands = commands[:i] + new_command + commands[i+1:]
            final_coordinates = get_final_coordinates(new_commands)
            possible_destinations.add(final_coordinates)
    
    return len(possible_destinations)

# Input
commands = input().strip()

# Output the number of distinct points
print(find_distinct_destinations(commands))