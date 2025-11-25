from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GoldTables").getOrCreate()

silver = "dbfs:/mnt/retail/silver/"
gold = "dbfs:/mnt/retail/gold/"

df = spark.read.format("delta").load(silver)

# DIM TABLES
dim_product = df.select("Product line").distinct().withColumnRenamed("Product line", "product_line")
dim_product.write.format("delta").mode("overwrite").save(gold + "dim_product")

# FACT SALES
fact_sales = df.select(
    "Invoice ID", "Date", "month", "year",
    "City", "Customer type", "Gender",
    "Product line", "Quantity", "Unit price",
    "Tax 5%", "Total", "gross_income"
)

fact_sales.write.format("delta").mode("overwrite").save(gold + "fact_sales")

print("Gold Fact & Dimension tables created!")
