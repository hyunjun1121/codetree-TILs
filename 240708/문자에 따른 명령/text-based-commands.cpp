#include <iostream>
#include <unordered_set>
#include <vector>
#include <string>

using namespace std;

// Function to simulate movement and return the final coordinates
pair<int, int> get_final_coordinates(const string& commands) {
    int direction = 0; // 0: north, 1: east, 2: south, 3: west
    int x = 0, y = 0;
    
    for (char command : commands) {
        if (command == 'L') {
            direction = (direction + 3) % 4;
        } else if (command == 'R') {
            direction = (direction + 1) % 4;
        } else if (command == 'F') {
            if (direction == 0) {
                y += 1;
            } else if (direction == 1) {
                x += 1;
            } else if (direction == 2) {
                y -= 1;
            } else if (direction == 3) {
                x -= 1;
            }
        }
    }
    
    return {x, y};
}

int find_distinct_destinations(const string& commands) {
    unordered_set<string> unique_points;
    vector<char> directions = {'L', 'R', 'F'};
    
    for (int i = 0; i < commands.size(); ++i) {
        for (char new_command : directions) {
            if (commands[i] == new_command) {
                continue;
            }
            
            string new_commands = commands;
            new_commands[i] = new_command;
            pair<int, int> final_coordinates = get_final_coordinates(new_commands);
            string point = to_string(final_coordinates.first) + "," + to_string(final_coordinates.second);
            unique_points.insert(point);
        }
    }
    
    return unique_points.size();
}

int main() {
    string commands;
    cin >> commands;
    
    cout << find_distinct_destinations(commands) << endl;
    
    return 0;
}