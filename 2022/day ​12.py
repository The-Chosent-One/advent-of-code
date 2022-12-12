# part 1 and 2

mountain = open("input.txt").read().split()

visited = [[None for _ in range(len(mountain[0]))] for _ in range(len(mountain))]

for index, l in enumerate(mountain):
    if "E" in l:
        end = (index, l.index("E"))
    if "S" in l:
        start = (index, l.index("S"))

done = False
queue = [end]
mountain[end[0]] = mountain[end[0]].replace("E","z")
mountain[start[0]] = mountain[start[0]].replace("S","a")
visited[end[0]][end[1]] = 0

for posx, posy in queue:
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x = posx + x
        next_y = posy + y

        if any([next_x < 0, next_y < 0, next_x == len(mountain), next_y == len(mountain[0])]):
            continue
        
        if ord(mountain[posx][posy]) - ord(mountain[next_x][next_y]) > 1:
            continue
        
        # replace if clause for part 2
        if (next_x, next_y) == start:
        # if mountain[next_x][next_y] == "a":
            done = True
            print(visited[posx][posy] + 1)
            break
        
        if visited[next_x][next_y] is not None:
            continue
        
        queue.append((next_x, next_y))
        visited[next_x][next_y] = visited[posx][posy] + 1
    
    if done:
        break
