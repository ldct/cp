#!/usr/bin/env pypy3

from typing import *
from functools import lru_cache

def move1(self):
    x = self.pos[0] + self.vel()[0]
    y = self.pos[1] + self.vel()[1]
    return (x, y)


def vel(vi):
    return [
        (1,0),
        (0,1),
        (-1,0),
        (0,-1)
    ][vi]

@lru_cache(None)
def state_from_1(width, height, x, y, vi):
    while True:
        n = (
            x + vel(vi)[0],
            y + vel(vi)[1]
        )
        if (0 <= n[0] < width) and (0 <= n[1] < height):
            return (vi, n)
        else:
            vi += 1
            vi %= 4

@lru_cache(None)
def state_from(width, height, x, y, vi, num_moves):
    if num_moves == 0: return (vi, (x, y))
    vi, (x, y) = state_from_1(width, height, x, y, vi)
    return state_from(width, height, x, y, vi, num_moves-1)

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = (0,0)
        self.vi = 0
        self.MODULUS = 4*((self.width + self.height)*2-4)


    def move(self, num: int) -> None:
        num %= self.MODULUS
        self.vi, self.pos = state_from(self.width, self.height, self.pos[0], self.pos[1], self.vi, num)

    def getPos(self) -> List[int]:
        return list(self.pos)


    def getDir(self) -> str:
        return ["East","North","West","South"
        ][self.vi]


obj = Robot(10, 10)
obj.move(1)
