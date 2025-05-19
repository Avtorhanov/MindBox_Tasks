from pyspark.sql import DataFrame

def get_product_category_pairs(products_df: DataFrame,
                                categories_df: DataFrame,
                                product_category_df: DataFrame) -> DataFrame:
    product_with_category_ids = products_df.join(
        product_category_df,
        products_df.id == product_category_df.product_id,
        how="left"
    )

    result = product_with_category_ids.join(
        categories_df,
        product_with_category_ids.category_id == categories_df.id,
        how="left"
    )

    return result.select(
        products_df["name"].alias("product_name"),
        categories_df["name"].alias("category_name")
    )
