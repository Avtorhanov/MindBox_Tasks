import pytest
from pyspark.sql import SparkSession
from src.product_category import get_product_category_pairs

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.master("local").appName("TestApp").getOrCreate()

def test_product_category_join(spark):
    products = spark.createDataFrame([
        (1, "Хлеб"),
        (2, "Кофе")
    ], ["id", "name"])

    categories = spark.createDataFrame([
        (1, "Выпечка")
    ], ["id", "name"])

    product_category = spark.createDataFrame([
        (1, 1)
    ], ["product_id", "category_id"])

    result = get_product_category_pairs(products, categories, product_category)
    actual = set((r["product_name"], r["category_name"]) for r in result.collect())

    assert ("Хлеб", "Выпечка") in actual
    assert ("Кофе", None) in actual
