import warnings


warnings.filterwarnings ("ignore")


from pyspark.sql import SparkSession


spark=SparkSession.builder.appName("RDD Operations Example").getOrCreate()

sc=spark.sparkContext


print("Import Sucessful.")


#Get SparkContext


SC=spark.sparkContext


# Create RDD from a Python list

data=[1,2,3,4,5]



rdd1= sc.parallelize(data)



print(rdd1.collect())


for i in data:
               print(i+2)