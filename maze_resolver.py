def maze_resolve(observation):

    start = observation[4]
    finish = observation[5]
    maze = observation[6]

    path = []
    my_stack = []
    current = start
    visited = [start]
    [my_stack.append(neighbour) for neighbour in get_neighbours(maze, current)]

    # for first step
    current = my_stack.pop()
    path.append(current)
    visited.append(current)
    [my_stack.append(neighbour) for neighbour in get_neighbours(maze, current)]

    while len(my_stack) > 0:

        current = my_stack.pop()

        if len([node for node in visited if node == current]) > 0:
            continue

        add_to_path(current, path, maze)
        visited.append(current)

        if current == finish:
            break

        [my_stack.append(neighbour) for neighbour in get_neighbours(maze, current)]

    print('my_stack:')
    print(my_stack)
    print('visited:')
    print(visited)
    return path


def get_neighbours(maze, position):
    neighbours = []
    for road in maze:
        if road[0] == position:   # if it current position in maze
            neighbours.append(road[1])
    # neighbours = [road[1] for road in maze if road[0] == position]
    return neighbours


def add_to_path(current, path, maze):

    prew = path.pop()
    right_path = True
    not_neighbour = 0
    while right_path:
        for neighbour in get_neighbours(maze, prew):
            if current == neighbour:
                path.append(prew)
                path.append(current)
                return True
            else:
                not_neighbour += 1
        prew = path.pop()
