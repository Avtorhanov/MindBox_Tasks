# 📦 geometry_lib

Библиотека для вычисления площади геометрических фигур и определения, является ли треугольник прямоугольным. Предназначена для внешнего использования клиентами.

---

## 🛠 Установка

Через локальный `pip install`:

pip install .

## 📌 Поддерживаемые фигуры

- Круг (`circle`)
- Треугольник (`triangle`)
- Квадрат (`square`)

---

## 🚀 Быстрый старт

```python
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
```

---

## 📚 Интерфейс

Все фигуры реализуют базовый интерфейс `Shape`:

```python
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...
```

Для треугольника дополнительно:

```python
def is_right(self) -> bool
```

## ❗ Ошибки

Если переданы некорректные аргументы (например, стороны не образуют треугольник), возбуждается `ValueError`.

---

## 📁 Структура пакета

```
geometry_lib/
├── geometry/
│   ├── __init__.py
│   ├── figures.py      # Определения фигур
│   └── factory.py      # Фабрика для создания фигур
├── __init__.py         # Публичный API
```

## 🧪 Тестирование

```bash
pytest
```

Тесты находятся в директории `tests/`.