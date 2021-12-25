import numpy as np
import random


'''
import pandas as pd
import pygame
'''
# just added this

ifPickup = 0
rows = 5
cols = 5
rewards = 0
pickUP = [(3, 5), (4, 2)]
dropOff = [(1, 1), (1, 5), (3, 3), (5, 5)]
pickup_blocks = {(3, 5): 8, (4, 2): 8}
dropoff_blocks = {(1, 1): 0, (1, 5): 0, (3, 3): 0, (5, 5): 0}
q_values = np.zeros((rows + 1, cols + 1, 2, 2, 2, 2, 2))  # Q(i,j,x,s,t,u,v)

coordinate = {
      (1, 1, 0): [-100, 0, 0, -100], (1, 2, 0): [-100, 0, 0, 0], (1, 3, 0): [-100, 0, 0, 0], (1, 4 ,0): [-100, 0, 0, 0], (1, 5, 0): [-100, -100, 0, 0]
    , (2, 1, 0): [0, 0, 0, -100],    (2, 2, 0): [0, 0, 0, 0],    (2, 3, 0): [0, 0, 0, 0],    (2, 4 ,0): [0, 0, 0, 0],    (2, 5, 0): [0, -100, 0, 0]
    , (3, 1, 0): [0, 0, 0, -100],    (3, 2, 0): [0, 0, 0, 0],    (3, 3, 0): [0, 0, 0, 0],    (3, 4 ,0): [0, 0, 0, 0],    (3, 5, 0): [0, -100, 0, 0]
    , (4, 1, 0): [0, 0, 0, -100],    (4, 2, 0): [0, 0, 0, 0],    (4, 3, 0): [0, 0, 0, 0],    (4, 4 ,0): [0, 0, 0, 0],    (4, 5, 0): [0, -100, 0, 0]
    , (5, 1, 0): [0, 0, -100, -100], (5, 2, 0): [0, 0, -100, 0], (5, 3, 0): [0, 0, -100, 0], (5, 4 ,0): [0, 0, -100, 0], (5, 5, 0): [0, -100, -100, 0]
    , (1, 1, 1): [-100, 0, 0, -100], (1, 2, 1): [-100, 0, 0, 0], (1, 3, 1): [-100, 0, 0, 0], (1, 4 ,1): [-100, 0, 0, 0], (1, 5, 1): [-100, -100, 0, 0]
    , (2, 1, 1): [0, 0, 0, -100],    (2, 2, 1): [0, 0, 0, 0],    (2, 3, 1): [0, 0, 0, 0],    (2, 4 ,1): [0, 0, 0, 0],    (2, 5, 1): [0, -100, 0, 0]
    , (3, 1, 1): [0, 0, 0, -100],    (3, 2, 1): [0, 0, 0, 0],    (3, 3, 1): [0, 0, 0, 0],    (3, 4 ,1): [0, 0, 0, 0],    (3, 5, 1): [0, -100, 0, 0]
    , (4, 1, 1): [0, 0, 0, -100],    (4, 2, 1): [0, 0, 0, 0],    (4, 3, 1): [0, 0, 0, 0],    (4, 4 ,1): [0, 0, 0, 0],    (4, 5, 1): [0, -100, 0, 0]
    , (5, 1, 1): [0, 0, -100, -100], (5, 2, 1): [0, 0, -100, 0], (5, 3, 1): [0, 0, -100, 0], (5, 4 ,1): [0, 0, -100, 0], (5, 5, 1): [0, -100, -100, 0]
    }

rewards_coordinate = {
    (1, 1): [-100, -1, -1, -100], (1, 2): [-100, -1, -1, 13], (1, 3): [-100, -1, -1, -1], (1, 4): [-100, 13, -1, -1], (1, 5): [-100, -100, -1, -1]
    , (2, 1): [13, -1, -1, -100], (2, 2): [-1, -1, -1, -1], (2, 3): [-1, -1, 13, -1], (2, 4): [-1, -1, -1, -1], (2, 5): [13, -100, 13, -1]
    , (3, 1): [-1, -1, -1, -100], (3, 2): [-1, 13, 13, -1], (3, 3): [-1, -1, -1, -1], (3, 4): [-1, 13, -1, 13], (3, 5): [-1, -100, -1, -1]
    , (4, 1): [-1, 13, -1, -100], (4, 2): [-1, -1, -1, -1], (4, 3): [13, -1, -1, 13], (4, 4): [-1, -1, -1, -1], (4, 5): [13, -100, 13, -1]
    , (5, 1): [-1, -1, -100, -100], (5, 2): [13, -1, -100, -1], (5, 3): [-1, -1, -100, -1], (5, 4): [-1, 13, -100, -1], (5, 5): [-1, -100, -100, -1]}

"""

    Q(direction, current coordinate) <- Q(direction, current coordinate) + learning_rate*[Rewards (of current coordinate) + discount_rate*Q(next direction, next coordinate) – Q(direction, current coordinate)]

"""

def PRandom(position):
    global ifPickup
    global rewards
    possible_direction = get_next_state(position)
    for (r, c, direction) in possible_direction: # [(1, 1), (2, 2), (3, 3)]
        if (r, c) in pickUP and ifPickup == 0 and pickup_blocks[(r, c)] != 0:
            ifPickup = 1
            pickup_blocks[(r, c)] += -1
            rewards += 13
            return (r, c, direction)
        elif (r, c) in dropOff and ifPickup == 1 and dropoff_blocks[(r, c)] != 4:
            ifPickup = 0
            dropoff_blocks[(r, c)] += 1
            rewards += 13
            return (r, c, direction)
    rewards += -1
    return random.choice(possible_direction)


def PGreedy(position):
    global ifPickup
    global rewards
    x, y = position
    possible_direction = get_next_state(position)
    qlist = []
    for (r, c, direction) in possible_direction:
        if (r, c) in pickUP and ifPickup == 0 and pickup_blocks[(r, c)] > 0:
            ifPickup = 1
            pickup_blocks[(r, c)] += -1
            rewards += 13
            return (r, c, direction)
        elif (r, c) in dropOff and ifPickup == 1 and dropoff_blocks[(r, c)] < 4:
            ifPickup = 0
            dropoff_blocks[(r, c)] += 1
            rewards += 13
            return (r, c, direction)
        else:
            if (r, c) not in pickUP or (r, c) not in dropOff:
                if not qlist:
                    qlist.append((r, c, direction))
                elif coordinate[(x, y, ifPickup)][qlist[-1][-1]] == coordinate[(x, y, ifPickup)][direction]:
                    qlist.append((r, c, direction))
                elif coordinate[(x, y, ifPickup)][qlist[-1][-1]] < coordinate[(x, y, ifPickup)][direction]:
                    qlist.clear()
                    qlist.append((r, c, direction))
    rewards += -1
    return random.choice(qlist)

def PExploit(position):
    if random.random() > 0.2:
        return PGreedy(position)
    else:
        return PRandom(position)

def get_next_state(position):
    x, y = position
    direction = []
    if x != 1:  # n
        direction.append((x - 1, y, 0))
    if y != 5:  # e
        direction.append((x, y + 1, 1))
    if x != 5:  # s
        direction.append((x + 1, y, 2))
    if y != 1:  # W
        direction.append((x, y - 1, 3))
    ###########################################################
    return direction


def run(starting_position, policy, learning_rate, discount_factor, ifSarsa):
    terminal_count = 1
    x, y = starting_position
    print("Terminal states of 500 steps")
    states = [(x,y,0,8,8,0,0,0,0)]
    q_s = [np.copy(q_values)] 
    for z in range(1, 501):
        old_reward = rewards
        if ifTerminal() == 1:
            print("Terminal State ", terminal_count, ": ")
            print("pick up locations: ")
            # print(pickup_blocks[(4, 2)], pickup_blocks[(3, 5)])
            print(pickup_blocks)
            print("drop off locations: ")
            print(dropoff_blocks[(1, 1)], dropoff_blocks[(1, 5)], dropoff_blocks[(3, 3)], dropoff_blocks[(5, 5)])
            print("steps: ", z, " rewards: ", rewards)
            print("----------------------------------")
            Reset(terminal_count)
            x = 5
            y = 1
            old_reward = 0
            """ # uncomment for experiment 4
            if terminal_count == 6:
                return
            """
            terminal_count += 1
        new_x, new_y, direction = PRandom((x, y))
        update_q_value(direction, (x, y, ifPickup), (new_x, new_y, ifPickup), discount_factor, learning_rate, (rewards - old_reward), ifSarsa, 'PRandom')
        x = new_x
        y = new_y
        states.append((x,y,ifPickup,pickup_blocks[(3,5)],pickup_blocks[(4,2)],dropoff_blocks[(1, 1)], dropoff_blocks[(1, 5)], dropoff_blocks[(3, 3)], dropoff_blocks[(5, 5)]))
        q_s.append(np.copy(q_values))

    print("Terminal states of 5500 steps")
    for z in range(501, 5501):
        old_reward = rewards
        if ifTerminal() == 1:
            print("Terminal State ", terminal_count, ": ")
            print("pick up locations: ")
            # print(pickup_blocks[(4, 2)], pickup_blocks[(3, 5)])
            print(pickup_blocks)
            print("drop off locations: ")
            print(dropoff_blocks[(1, 1)], dropoff_blocks[(1, 5)], dropoff_blocks[(3, 3)], dropoff_blocks[(5, 5)])
            print("steps: ", z, " rewards: ", rewards)
            print("----------------------------------")
            Reset(terminal_count)
            x = 5
            y = 1
            old_reward = 0
            """ # uncomment for experiment 4
            if terminal_count == 6:
                return
            """
            terminal_count += 1
        if policy == 'PRandom':
            new_x, new_y, direction = PRandom((x, y))
        elif policy == 'PGreedy':
            new_x, new_y, direction = PGreedy((x, y))
        elif policy == 'PExploit':
            new_x, new_y, direction = PExploit((x, y))
            # print(new_x, new_y, direction)
        update_q_value(direction, (x, y, ifPickup), (new_x, new_y, ifPickup), discount_factor, learning_rate, (rewards - old_reward), ifSarsa, policy)
        x = new_x
        y = new_y
        states.append((x,y,ifPickup,pickup_blocks[(3,5)],pickup_blocks[(4,2)],dropoff_blocks[(1, 1)], dropoff_blocks[(1, 5)], dropoff_blocks[(3, 3)], dropoff_blocks[(5, 5)]))
        q_s.append(np.copy(q_values))
    return states,q_s
    


def sarsa_direction(position, policy):
    x, y, trash = position
    possible_direction = get_next_state((x, y))
    qlist = []
    for (r, c, direction) in possible_direction:
        if (r, c) in pickUP and ifPickup == 0 and pickup_blocks[(r, c)] > 0:
            return direction
        elif (r, c) in dropOff and ifPickup == 1 and dropoff_blocks[(r, c)] < 4:
            return direction
    for (r, c, direction) in possible_direction:
        if policy == 'PGreedy':
            if not qlist:
                qlist.append(direction)
            elif coordinate[(x, y, trash)][qlist[-1]] == coordinate[(x, y, trash)][direction]:
                qlist.append(direction)
            elif coordinate[(x, y, trash)][qlist[-1]] < coordinate[(x, y, trash)][direction]:
                qlist.clear()
                qlist.append(direction)
        elif policy == 'PRandom':
            qlist.append(direction)
        else:
            if random.random() > 0.2:
                return sarsa_direction(position, 'PGreedy')
            else:
                return sarsa_direction(position, 'PRandom')
    return random.choice(qlist)


def update_q_value(current_direction, current_coordinate, next_coordinate, learning_rate, discount, reward, sarsa, policy):
    if sarsa == 0:
        coordinate[current_coordinate][current_direction] = round(((1 - learning_rate) * (coordinate[current_coordinate][current_direction])) + (learning_rate * ((reward) + (discount * max(coordinate[next_coordinate])))), 3)
    else:
        coordinate[current_coordinate][current_direction] = round((coordinate[current_coordinate][current_direction]) + (learning_rate * (reward + (discount * coordinate[next_coordinate][sarsa_direction(next_coordinate, policy)]) - coordinate[current_coordinate][current_direction])), 3)

def ifTerminal():
    if dropoff_blocks[(1, 1)] == 4 and dropoff_blocks[(1, 5)] == 4 and dropoff_blocks[(3, 3)] == 4 and dropoff_blocks[(5, 5)] == 4:
        return 1
    else:
        return 0

def Reset(terminal_condition):
    # if terminal_condition <= 3:  # for experiment 4 uncomment the if statement and indent lines 214 and 215
    pickup_blocks[(4, 2)] = 8
    pickup_blocks[(3, 5)] = 8
    dropoff_blocks[(1, 1)] = 0
    dropoff_blocks[(1, 5)] = 0
    dropoff_blocks[(3, 3)] = 0
    dropoff_blocks[(5, 5)] = 0
    global rewards
    global ifPickup
    rewards = 0
    ifPickup = 0
    """
    if terminal_condition == 3:   # for experiment 4 uncomment these if statements
        print("changed pickup locations")
        pickup_blocks[(3, 1)] = 8
        pickup_blocks[(1, 3)] = 8
        del pickup_blocks[(4, 2)]
        del pickup_blocks[(3, 5)]
        global pickUP
        pickUP = [(3, 1), (1, 3)]
    if terminal_condition > 3:
        pickup_blocks[(3, 1)] = 8
        pickup_blocks[(1, 3)] = 8
    """



run((5, 1), 'PExploit', 0.30, 0.5, 1)
#for key, value in coordinate.items():
    #print(key, " : ", value)



