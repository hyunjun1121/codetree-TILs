def possible_destinations(commands):
    def simulate(cmds):
        direction = 0  # 0: north, 1: east, 2: south, 3: west
        x, y = 0, 0
        for cmd in cmds:
            if cmd == 'L':
                direction = (direction - 1) % 4
            elif cmd == 'R':
                direction = (direction + 1) % 4
            elif cmd == 'F':
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                elif direction == 3:
                    x -= 1
        return (x, y)
    
    destinations = set()
    
    for i in range(len(commands)):
        for new_cmd in 'LRF':
            if commands[i] != new_cmd:
                new_commands = commands[:i] + new_cmd + commands[i + 1:]
                new_destination = simulate(new_commands)
                destinations.add(new_destination)
    
    return len(destinations)

# Example usage:
commands = input().strip()
print(possible_destinations(commands))