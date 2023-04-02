from typing import List
from random import random

EPS = 1e-9

class Map:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def len(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5
    
    def norm(self, l=1.0):
        if self.len() > EPS:
            return Point(self.x / self.len() * l, self.y / self.len() * l)
        
        return Point(0, 0)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    def __add__(self, pt):
        obj = Point(self.x + pt.x, self.y + pt.y)
        return obj

    def __sub__(self, pt):
        obj = Point(self.x - pt.x, self.y - pt.y)
        return obj
    
    def __div__(self, d):
        obj = Point(self.x / d, self.y / d)
        return obj

class Rectangle:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def center(self):
        return Point(self._x + self._width / 2, self._y + self._height / 2)
    
    def move(self, delta: Point, map: Map):
        self._x += delta.x
        self._y += delta.y

        if self._x < 0:
            self._x = 0

        if self._y < 0:
            self._y = 0

        if map.width <= self._x + self._width:
            self._x = map.width - self._width

        if map.height <= self._y + self._height:
            self._y = map.height - self._height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

def cross(a: Rectangle, b: Rectangle):
    min_x = max(a.x, b.x)
    min_y = max(a.y, b.y)
    max_x = min(a.x + a.width, b.x + b.width)
    max_y = min(a.y + a.height, b.y + b.height)

    if min_x >= max_x or min_y >= max_y:
        return None

    return Rectangle(min_x, min_y, max_x - min_x, max_y - min_y)


def solve(map: Map, rectangles: List[Rectangle]):
    moved = False
    for a in rectangles:
        delta = Point(0, 0)

        for b in rectangles:
            if a is b:
                continue
        
            c = cross(a, b)

            if not c:
                continue
            
            direction = (a.center() - c.center())
            delta += direction.norm(c.area())

        if delta.len() > EPS:
            moved = True
            a.move(delta.norm(), map)

    return moved
                

