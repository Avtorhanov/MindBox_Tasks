import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from geometry_lib.geometry.factory import ShapeFactory
from geometry_lib.geometry.figures import Triangle


def test_circle_area():
    circle = ShapeFactory.create("circle", radius=1)
    assert round(circle.area(), 5) == round(3.14159, 5)


def test_triangle_area():
    triangle = ShapeFactory.create("triangle", a=3, b=4, c=5)
    assert round(triangle.area(), 5) == 6.0


def test_triangle_is_right():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right()


def test_triangle_not_right():
    triangle = Triangle(3, 4, 6)
    assert not triangle.is_right()



def test_circle_area():
    circle = ShapeFactory.create("circle", radius=1)
    assert round(circle.area(), 5) == round(3.14159, 5)


def test_triangle_area():
    triangle = ShapeFactory.create("triangle", a=3, b=4, c=5)
    assert round(triangle.area(), 5) == 6.0


def test_triangle_is_right():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right()


def test_triangle_not_right():
    triangle = Triangle(3, 4, 6)
    assert not triangle.is_right()
