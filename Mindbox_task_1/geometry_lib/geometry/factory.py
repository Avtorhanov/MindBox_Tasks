from .figures import Circle, Triangle, Square, Shape


class ShapeFactory:
    @staticmethod
    def create(shape_type: str, **kwargs) -> Shape:
        if shape_type == "circle":
            return Circle(kwargs["radius"])
        elif shape_type == "triangle":
            return Triangle(kwargs["a"], kwargs["b"], kwargs["c"])
        elif shape_type == "square":
            return Square(kwargs["side"])
        else:
            raise ValueError(f"Неизвестный тип фигуры: {shape_type}")
