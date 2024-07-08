def calculate_positions(commands):
    n = len(commands)
    x, y = 0, 0
    direction = 0  # 0: 북, 1: 동, 2: 남, 3: 서

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    positions = [(0, 0, 0)]  # (x, y, direction)

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
        for new_command in ['L', 'R', 'F']:
            if command_string[i] != new_command:
                x, y, direction = positions[i]

                if new_command == 'L':
                    direction = (direction - 1) % 4
                elif new_command == 'R':
                    direction = (direction + 1) % 4
                elif new_command == 'F':
                    x += dx[direction]
                    y += dy[direction]

                if i + 1 < n:
                    remaining_positions = calculate_positions(command_string[i+1:])
                    for rx, ry, rdir in remaining_positions:
                        x += dx[direction] * rx
                        y += dy[direction] * ry
                        direction = (direction + rdir) % 4
                        unique_positions.add((x, y))
                else:
                    unique_positions.add((x, y))

    return len(unique_positions)

# Example usage
command_string = input().strip()
print(different_positions(command_string))