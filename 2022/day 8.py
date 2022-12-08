import numpy as np

# part 1
grid = np.array([[*map(int, s)] for s in open("input.txt").read().split()])
visible = np.zeros(grid.shape)
# all four edges
visible[0, :] = 1
visible[-1, :] = 1
visible[:, 0] = 1
visible[:, -1] = 1

for transform in (lambda g: g, np.fliplr, lambda g: g.T, lambda g: np.fliplr(g.T)):
    for index, trees in enumerate(transform(grid)[1:-1], 1):
        highest = -1

        for inner_index, tree in enumerate(trees):
            if tree > highest:
                highest = tree
                transform(visible)[index][inner_index] = 1

print(sum(sum(visible)))

# part 2
grid = np.array([[*map(int, s)] for s in open("input.txt").read().split()])
scene = np.ones(grid.shape)
# all four edges
scene[0, :] = 0
scene[-1, :] = 0
scene[:, 0] = 0
scene[:, -1] = 0

for transform in (lambda g: g, np.fliplr, lambda g: g.T, lambda g: np.fliplr(g.T)):
    for index, trees in enumerate(transform(grid)[1:-1], 1):
        scene_count = []

        for inner_index, tree_under_consideration in enumerate(trees):
            default_scene = 0
            for tree in trees[:inner_index][::-1]:
                default_scene += 1
                if tree >= tree_under_consideration:
                    break

            scene_count.append(default_scene)
        
        transform(scene)[index] *= scene_count

print(scene.flatten().max())
