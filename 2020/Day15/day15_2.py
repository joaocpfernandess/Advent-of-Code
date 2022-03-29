start = [5, 1, 9, 18, 13, 8, 0]

def game(startingnums, turns):
    memory = {}
    for i in range(len(startingnums)):
        memory[startingnums[i]] = [1, i, None]
    said = startingnums[i]
    for i in range(len(startingnums), turns):
        if memory[said][0] == 1:    # If the most recent number has only been said once
            said = 0
        else:
            said = memory[said][1] - memory[said][2]
        if said not in memory:       # If the just-announced number isn't in memory, create a memory spot
            memory[said] = [1, i, None]
        else:
            memory[said][0] += 1
            memory[said][2] = memory[said][1]
            memory[said][1] = i
    return said


print(game(start, 30000000))
