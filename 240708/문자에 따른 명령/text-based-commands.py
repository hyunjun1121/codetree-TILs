def possible_destinations(commands):
    from functools import lru_cache

    # Define movement vectors for north, east, south, and west
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    @lru_cache(None)
    def simulate(cmds):
        direction = 0  # 0: north, 1: east, 2: south, 3: west
        x, y = 0, 0
        for cmd in cmds:
            if cmd == 'L':
                direction = (direction - 1) % 4
            elif cmd == 'R':
                direction = (direction + 1) % 4
            elif cmd == 'F':
                move_x, move_y = movements[direction]
                x += move_x
                y += move_y
        return (x, y)
    
    destinations = set()
    
    for i in range(len(commands)):
        for new_cmd in 'LRF':
            if commands[i] != new_cmd:
                new_commands = commands[:i] + new_cmd + commands[i + 1:]
                new_destination = simulate(tuple(new_commands))
                destinations.add(new_destination)
    
    return len(destinations)

# Example usage:
commands = input().strip()
print(possible_destinations(commands))