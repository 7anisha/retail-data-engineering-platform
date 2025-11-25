from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("RetailCleaning").getOrCreate()

raw = "dbfs:/mnt/retail/raw/"
silver = "dbfs:/mnt/retail/silver/"

df = spark.read.format("delta").load(raw)

clean_df = (
    df.withColumn("Date", to_date("Date", "dd/MM/yyyy"))
      .withColumn("gross_income", col("Unit price") * col("Quantity"))
      .withColumn("month", month("Date"))
      .withColumn("year", year("Date"))
      .dropDuplicates()
)

clean_df.write.format("delta").mode("overwrite").save(silver)
print("Silver table created!")
