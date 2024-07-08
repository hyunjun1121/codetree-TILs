def possible_destinations(commands):
    # Map of direction changes
    direction_changes = {
        'L': -1,
        'R': 1,
        'F': 0
    }

    # Map of movements in (x, y) coordinates for each direction
    movements = [
        (0, 1),  # North
        (1, 0),  # East
        (0, -1), # South
        (-1, 0)  # West
    ]
    
    def simulate(cmds):
        direction = 0  # Start facing north
        x, y = 0, 0
        for cmd in cmds:
            if cmd == 'F':
                move_x, move_y = movements[direction]
                x += move_x
                y += move_y
            else:
                direction = (direction + direction_changes[cmd]) % 4
        return (x, y)
    
    original_destination = simulate(commands)
    destinations = {original_destination}
    
    for i, cmd in enumerate(commands):
        for new_cmd in 'LRF':
            if cmd != new_cmd:
                new_commands = commands[:i] + new_cmd + commands[i + 1:]
                new_destination = simulate(new_commands)
                destinations.add(new_destination)
    
    return len(destinations)

# Example usage:
commands = input().strip()
print(possible_destinations(commands))