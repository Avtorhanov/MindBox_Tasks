from build.lib.geometry.factory import ShapeFactory

# Круг радиусом 3
circle = ShapeFactory.create("circle", radius=3)
print(circle.area())  # → 28.274...

# Треугольник со сторонами 3, 4, 5
triangle = ShapeFactory.create("triangle", a=3, b=4, c=5)
print(triangle.area())      # → 6.0
print(triangle.is_right())  # → True

# Квадрат со стороной 4
square = ShapeFactory.create("square", side=4)
print(square.area())  # → 16
