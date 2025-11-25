from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RetailIngestion") \
    .getOrCreate()

raw_path = "dbfs:/mnt/retail/raw/supermarket_sales.csv"

df = spark.read.csv("/Workspace/Files/supermarket_sales.csv", header=True, inferSchema=True)

df.write.format("delta").mode("overwrite").save(raw_path)

print("Ingestion complete → RAW Zone (Bronze)")
