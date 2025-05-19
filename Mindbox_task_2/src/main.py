from pyspark.sql import SparkSession
from product_category import get_product_category_pairs

def main():
    spark = SparkSession.builder.master("local").appName("ProductCategoryJoin").getOrCreate()

    products = spark.createDataFrame([
        (1, "Хлеб"),
        (2, "Молоко"),
        (3, "Сыр"),
        (4, "Пельмени"),
        (5, "Кофе")
    ], ["id", "name"])

    categories = spark.createDataFrame([
        (1, "Молочные"),
        (2, "Замороженные"),
        (3, "Выпечка")
    ], ["id", "name"])

    product_category = spark.createDataFrame([
        (1, 3),
        (2, 1),
        (3, 1),
        (4, 2)
    ], ["product_id", "category_id"])

    result = get_product_category_pairs(products, categories, product_category)
    result.show(truncate=False)

if __name__ == "__main__":
    main()
