# part 1
head_moves = open("input.txt").read().split("\n")

moves = set()
T = [0, 0]
H = [0, 0]

for direction,_,*steps in head_moves:
    steps = int("".join(steps))
    if direction in "LR":
        H[0] += steps * ("L R".index(direction) - 1)
    if direction in "D U":
        H[1] += steps * ("D U".index(direction) - 1)

    x_diff, y_diff = [abs(a-b) for a,b in zip(T,H)]
    (hx, hy), (tx, ty) = H, T

    if x_diff and y_diff:
        x_diff -= 1
        y_diff -= 1
        if x_diff:
            T[0] += (-1)**((hx > tx) + 1)
            T[1] = hy
        if y_diff:
            T[0] = hx
            T[1] += (-1)**((hy > ty) + 1)
    
    (hx, hy), (tx, ty) = H, T
    if x_diff:
        moves |= {(x, ty) for x in range(tx, hx) or range(tx, hx, -1)}
        T[0] += hx - tx - (-1)**((hx > tx) + 1)
    if y_diff:
        moves |= {(tx, y) for y in range(ty, hy) or range(ty, hy, -1)}
        T[1] += hy - ty - (-1)**((hy > ty) + 1)

print(len(moves))

# part 2
head_moves = open("input.txt").read().split("\n")

moves = {(0, 0)}
R = [[0, 0] for _ in range(10)]

for direction,_,*steps in head_moves:
    steps = int("".join(steps))

    for s in range(steps):
        if direction in "LR":
            R[0][0] += ("L R".index(direction) - 1)
        if direction in "D U":
            R[0][1] += ("D U".index(direction) - 1)
        
        for i in range(9):
            H, T = R[i], R[i+1]

            x_diff, y_diff = [abs(a-b) for a,b in zip(T,H)]
            (hx, hy), (tx, ty) = H, T

            if x_diff and y_diff:
                x_diff -= 1
                y_diff -= 1
                if x_diff and y_diff:
                    R[i+1][0] += (-1)**((hx > tx) + 1)
                    R[i+1][1] += (-1)**((hy > ty) + 1)

                elif x_diff:
                    R[i+1][0] += (-1)**((hx > tx) + 1)
                    R[i+1][1] = hy
                elif y_diff:
                    R[i+1][0] = hx
                    R[i+1][1] += (-1)**((hy > ty) + 1)
            
            (hx, hy), (tx, ty) = H, T
            if x_diff:
                moves |= {(x, ty) for x in range(tx, hx) or range(tx, hx, -1)} if i == 8 else set()
                R[i+1][0] += hx - tx - (-1)**((hx > tx) + 1)
            if y_diff:
                moves |= {(tx, y) for y in range(ty, hy) or range(ty, hy, -1)} if i == 8 else set()
                R[i+1][1] += hy - ty - (-1)**((hy > ty) + 1)
                
print(len(moves))
