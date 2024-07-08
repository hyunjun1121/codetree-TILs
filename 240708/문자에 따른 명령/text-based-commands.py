def get_distinct_destinations(commands):
    # Initial direction is north (index 0)
    directions = ['N', 'E', 'S', 'W']
    moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    command_list = list(commands)
    n = len(command_list)

    def simulate(commands):
        x, y = 0, 0
        direction_index = 0  # Start facing north
        for command in commands:
            if command == 'L':
                direction_index = (direction_index - 1) % 4
            elif command == 'R':
                direction_index = (direction_index + 1) % 4
            elif command == 'F':
                dx, dy = moves[directions[direction_index]]
                x += dx
                y += dy
        return (x, y)

    # Original destination
    original_destination = simulate(command_list)
    distinct_destinations = set()
    distinct_destinations.add(original_destination)

    # Iterate over each command and change it
    for i in range(n):
        original_command = command_list[i]
        for new_command in 'LRF':
            if new_command != original_command:
                new_commands = command_list[:]
                new_commands[i] = new_command
                new_destination = simulate(new_commands)
                distinct_destinations.add(new_destination)

    return len(distinct_destinations)

# Read input
commands = input().strip()

# Output the number of distinct destination points
print(get_distinct_destinations(commands))