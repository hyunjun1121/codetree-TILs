def calculate_final_position(commands):
    # 方向向量：北、东、南、西
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0  # 起始坐标
    direction_index = 0  # 初始方向：北
    
    for command in commands:
        if command == 'L':
            direction_index = (direction_index - 1) % 4
        elif command == 'R':
            direction_index = (direction_index + 1) % 4
        elif command == 'F':
            x += directions[direction_index][0]
            y += directions[direction_index][1]
    
    return (x, y)

def distinct_destinations(commands):
    n = len(commands)
    unique_positions = set()

    # 原命令序列的终点
    original_position = calculate_final_position(commands)
    unique_positions.add(original_position)

    for i in range(n):
        if commands[i] == 'L' or commands[i] == 'R' or commands[i] == 'F':
            for new_command in 'LRF':
                if commands[i] != new_command:
                    new_commands = commands[:i] + new_command + commands[i+1:]
                    new_position = calculate_final_position(new_commands)
                    unique_positions.add(new_position)
    
    return len(unique_positions)

# 输入处理
commands = input().strip()
print(distinct_destinations(commands))