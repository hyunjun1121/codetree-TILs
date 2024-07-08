def get_final_position(commands):
    x, y = 0, 0
    direction = 0  # Start facing north
    # Directions: 0 = north, 1 = east, 2 = south, 3 = west
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            dx, dy = directions[direction]
            x += dx
            y += dy
            
    return (x, y)

def count_distinct_destinations(commands):
    distinct_destinations = set()
    n = len(commands)
    
    for i in range(n):
        for replacement in 'LRF':
            if commands[i] == replacement:
                continue
            # Create a new command string with the i-th command replaced
            new_commands = commands[:i] + replacement + commands[i+1:]
            final_position = get_final_position(new_commands)
            distinct_destinations.add(final_position)
    
    return len(distinct_destinations)

# Read input
commands = input().strip()

# Get the number of distinct possible destinations
result = count_distinct_destinations(commands)
print(result)