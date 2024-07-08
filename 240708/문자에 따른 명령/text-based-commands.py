def count_distinct_positions(commands):
    # Directions mapping: North, East, South, West
    directions = ['N', 'E', 'S', 'W']
    
    def move(x, y, direction):
        if direction == 'N':
            return x, y + 1
        elif direction == 'E':
            return x + 1, y
        elif direction == 'S':
            return x, y - 1
        elif direction == 'W':
            return x - 1, y
    
    def new_direction(curr_dir, turn):
        idx = directions.index(curr_dir)
        if turn == 'L':
            idx = (idx - 1) % 4
        elif turn == 'R':
            idx = (idx + 1) % 4
        return directions[idx]
    
    n = len(commands)
    distinct_positions = set()
    
    # Simulate each command being the incorrect one
    for i in range(n):
        for new_command in 'LRF':
            if commands[i] == new_command:
                continue
            
            x, y = 0, 0
            direction = 'N'
            
            # Apply commands with the ith one corrected
            for j in range(n):
                cmd = new_command if j == i else commands[j]
                if cmd == 'F':
                    x, y = move(x, y, direction)
                else:
                    direction = new_direction(direction, cmd)
            
            distinct_positions.add((x, y))
    
    return len(distinct_positions)

# Example usage
commands = input().strip()
print(count_distinct_positions(commands))