from geometry.factory import ShapeFactory


def main():
    while True:
        print("\nВыберите фигуру для расчета площади:")
        print("1 - Круг")
        print("2 - Треугольник")
        print("3 - Квадрат")

        choice = input("Введите номер фигуры: ")

        try:
            if choice == "1":
                radius = float(input("Введите радиус круга: "))
                circle = ShapeFactory.create("circle", radius=radius)
                print(f"Площадь круга: {circle.area():.2f}")

            elif choice == "2":
                a = float(input("Введите сторону a: "))
                b = float(input("Введите сторону b: "))
                c = float(input("Введите сторону c: "))
                triangle = ShapeFactory.create("triangle", a=a, b=b, c=c)
                print(f"Площадь треугольника: {triangle.area():.2f}")
                print(f"Треугольник прямоугольный? {'Да' if triangle.is_right() else 'Нет'}")

            elif choice == "3":
                side = float(input("Введите длину стороны квадрата: "))
                square = ShapeFactory.create("square", side=side)
                print(f"Площадь квадрата: {square.area():.2f}")

            else:
                print("Неверный выбор. Попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка: {e}")


        cont = input("\nХотите выполнить ещё один расчёт? (y/д — да, n/н — нет): ").strip().lower()
        if cont in ("n", "н", "no", "нет"):
            print("Завершение работы. До свидания!")
            break


if __name__ == "__main__":
    main()
