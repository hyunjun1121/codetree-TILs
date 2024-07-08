def simulate(commands):
    x, y = 0, 0
    direction = 0  # Start facing north
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    positions = [(0, 0)]
    directions_at_each_step = [direction]

    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            dx, dy = directions[direction]
            x += dx
            y += dy
        positions.append((x, y))
        directions_at_each_step.append(direction)

    return positions, directions_at_each_step

def count_distinct_destinations(commands):
    n = len(commands)
    initial_positions, initial_directions = simulate(commands)
    distinct_destinations = set()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(n):
        for replacement in 'LRF':
            if commands[i] == replacement:
                continue
            
            # Recalculate the final position after changing the i-th command
            x, y = initial_positions[i]
            direction = initial_directions[i]

            if replacement == 'L':
                direction = (direction - 1) % 4
            elif replacement == 'R':
                direction = (direction + 1) % 4
            elif replacement == 'F':
                dx, dy = directions[direction]
                x += dx
                y += dy

            # Follow the remaining commands
            for command in commands[i+1:]:
                if command == 'L':
                    direction = (direction - 1) % 4
                elif command == 'R':
                    direction = (direction + 1) % 4
                elif command == 'F':
                    dx, dy = directions[direction]
                    x += dx
                    y += dy

            distinct_destinations.add((x, y))

    return len(distinct_destinations)

# Read input
import sys
input = sys.stdin.read().strip()

# Get the number of distinct possible destinations
result = count_distinct_destinations(input)
print(result)