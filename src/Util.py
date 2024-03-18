import random
from math import comb

class Point:
    def __init__(self, x, y) -> None:
        self.x: float = x
        self.y: float = y

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

color_list = [[0, generate_random_color()] for i in range(6)]
iterationNow = 0

def GetMiddlePoint(point1: Point, point2: Point) -> Point:
    point = Point((point1.x + point2.x)/2, (point1.y + point2.y)/2)
    return point

def getCombination(n: int, r: int):
    return comb(n, r)