import os
import os.path as osp
import operator
import numpy as np

# create cost class to save cost value for each node
class Node():
    """
    Node class for A* path finding
    """
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other_node):
        return self.position == other_node.position

    def move_to(self, direction):
        new_postion = (self.position[0] + direction[0], self.position[1] + direction[1])
        new_node = Node(parent=self, position=new_postion)
        return new_node

def is_valid_node(map, node):
    """
    check if node is inside map and not on any obstacle
    """
    inside_map_cond = node.position[0] >= 0 and \
                      node.position[1] >= 0 and \
                      node.position[0] < map.shape[0] and \
                      node.position[1] < map.shape[1]
    if not inside_map_cond:
        return False
    if map[node.position[0], node.position[1]] == 1:
        return False
    return True

def a_star_maze(current_map, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    if current_map[start[0], start[1]] == 1:
        print("Start at obstactle, rerun")
        return 
    if current_map[end[0], end[1]] == 1:
        print("End at obstactle, rerun")
        return

    # Create start and end node    
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0


    open_list = list()
    close_list = list()

    open_list.append(start_node)

    # 8 around squares of a node 
    possible_directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (1, -1), (1, 0), (1, 1)]
    while len(open_list) > 0:

        # get current node with
        list_f_value = [node.f for node in open_list]
        current_index = list_f_value.index(max(list_f_value))

        current_node = open_list[current_index]
        open_list.pop(current_index)
        print(current_node.position)        
        children = []
        for pos_direction in possible_directions:
            new_position = tuple(map(operator.add, current_node.position, pos_direction))
            new_node = Node(parent=current_node, position=new_position)
            if new_node.position == end_node.position:
                current = current_node
                path = list()
                while current_node is not None:
                    path.append(current.position)
                    current = current.parent
                    print(current)
                return path
            # print(new_node)
            if not is_valid_node(current_map, new_node):
                continue
            new_node.g = current_node.g + 1
            new_node.h = np.linalg.norm(tuple(map(operator.sub, end_node.position, new_node.position)))
            new_node.f = new_node.g + new_node.h
            children.append(new_node)

        for child in children:
            if child in close_list:
                continue
            for open_node in open_list:
                if open_node == child and child.g > open_node.g:
                    continue
            open_list.append(child)                


if __name__ == "__main__":
    # create map
    map_array = np.zeros(64)
    map_array[:8] = 1
    np.random.shuffle(map_array)
    my_map = np.reshape(map_array, (8, 8))
    start, end = (0, 0), (6, 7)
    path = a_star_maze(my_map, start, end)
    print(my_map)
    print(path)
