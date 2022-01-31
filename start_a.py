import car_maze as cm
import time
import maze_resolver

env = cm.CarMazeEnv("open")

#################################################
# Observation space value meanings by list index:
# 0 - up       (values: 0 - road blocked,  1 - road available)
# 1 - down
# 2 - left
# 3 - right
# 4 - ID position of car
# 5 - ID position of gold
# 6 - roads / possible moves of the maze. Tuple of two ID values (from, to)
#
###########################
# Action space values
# 0 - up
# 1 - down
# 2 - left
# 3 - right

#####################################
# You code starts here
#####################################

print("0 - up")
print("1 - down")
print("2 - left")
print("3 - right")


def spliting_string(text):
    return text.split('-', 1)


for i_episode in range(1):
    observation = env.reset()
    env.render()
    print(observation[5])  # gold
    path = maze_resolver.maze_resolve(observation)

    print('path:')
    print(path)
    path.reverse()

    for t in range(200000):
        env.render()

        # # # --------------------------------------------
        # # # example code
        # # # --------------------------------------------
        # action = env.action_space.sample()
        time.sleep(0.15)
        eile = path.pop()

        # current
        x_asis = observation[4].split('-')[0]
        y_asis = observation[4].split('-')[1]

        # move
        x = eile.partition("-")[0]
        y = eile.partition("-")[2]
        print("X: " + x + " Y: " + y)

        if int(x) > int(x_asis):
            action = 3
        elif int(x) < int(x_asis):
            action = 2
        elif int(y) > int(y_asis):
            action = 0
        elif int(y) < int(y_asis):
            action = 1

        observation, reward, done, info = env.step(action)
        print(observation[6])

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print("Reward - " + str(reward))
            break
        # # --------------------------------------------
        # # end of example code
        # # --------------------------------------------


#####################################
# You code ends here
#####################################

env.close()
