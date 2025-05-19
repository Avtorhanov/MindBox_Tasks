# Mindbox_task_2

Тестовое задание: обработка данных о продуктах и категориях с помощью PySpark.

## 📌 Задача

Необходимо реализовать метод, который возвращает:

1. Все пары **"Имя продукта – Имя категории"**, включая продукты без категорий.
2. Имена продуктов, **не имеющих категорий**.

## 📁 Структура проекта

```

.
├── main.py                        # Точка входа в приложение
├── processor.py                   # Основная логика обработки Spark DataFrame
├── tests/
│   └── test_product_category.py   # Юнит-тесты (pytest)
├── requirements.txt               # Зависимости
└── README.md                      # Описание проекта

````

## 🚀 Запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt


2. Запустите скрипт:

   ```bash
   python main.py
   ```

## ✅ Тестирование

```bash
pytest
```

## 🛠 Используемые технологии

* Python 3.10+
* PySpark
* pytest

## 📎 Пример входных данных

```python
products = [
    {"product_id": 1, "product_name": "Телефон", "category_id": 10},
    {"product_id": 2, "product_name": "Ноутбук", "category_id": None},
]

categories = [
    {"category_id": 10, "category_name": "Электроника"},
]
```
