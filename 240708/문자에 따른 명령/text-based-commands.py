def get_new_position(commands):
    # 초기 위치와 방향 설정 (북쪽을 향함)
    x, y = 0, 0
    direction = 0  # 0: 북, 1: 동, 2: 남, 3: 서

    # 방향 벡터 설정 (북, 동, 남, 서 순)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for command in commands:
        if command == 'L':
            direction = (direction - 1) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'F':
            x += dx[direction]
            y += dy[direction]

    return (x, y)

def different_positions(command_string):
    n = len(command_string)
    unique_positions = set()
    
    # 모든 가능한 잘못된 명령을 교정하여 도착 지점을 계산
    for i in range(n):
        for new_command in ['L', 'R', 'F']:
            if command_string[i] != new_command:
                new_commands = command_string[:i] + new_command + command_string[i+1:]
                final_position = get_new_position(new_commands)
                unique_positions.add(final_position)
    
    return len(unique_positions)

# 예제 사용
command_string = input().strip()
print(different_positions(command_string))