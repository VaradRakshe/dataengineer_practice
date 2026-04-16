from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("JSON Example") \
    .getOrCreate()

df_json = spark.read.json(r"C:\Users\91838\Downloads\sample1.json")
df_json.show()

# Multiline JSON
df_json = spark.read.option("multiline", True).json(r"C:\Users\91838\Downloads\sample1.json")
df_json.show()
