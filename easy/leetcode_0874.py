"""
    1、机器人路径
"""

from email.errors import ObsoleteHeaderDefect


def robotSim(commands, obstacles):
    pos = [0, 0]
    deg = 90
    ans = 0
    obstaclesSet = set(map(tuple, obstacles))

    for command in commands:
        if command==-1:
            deg = (deg+270)%360
        elif command==-2:
            deg = (deg+90) % 360
        else:
            if deg == 0:
                i = 0
                while i<command and not(pos[0]+1,pos[1]) in obstaclesSet:
                    pos[0] += 1
                    i += 1
            if deg == 90:
                i = 0
                while i<command and not(pos[0],pos[1]+1) in obstaclesSet:
                    pos[1] += 1
                    i += 1
            if deg==180:
                i = 0
                while i<command and not (pos[0]-1, pos[1]) in obstacles:
                    pos[0] -= 1
                    i += 1
            if deg == 270:
                i = 0
                while i < command and not (pos[0], pos[1]-1) in obstacles:
                    pos[1] -= 1
                    i += 1
            ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
    return ans

commands = [4,-1,3]
obstacles = []
result = robotSim(commands, obstacles)
print(result)