s3_path='s3://asif-test1/new_cust/new/city_table.csv'
from pyspark.sql import SparkSession
data=spark.read.csv(s3_path,header=True)
data.show()

data.write.partitionBy("city").parquet("s3://asif-test1/new_cust/new1")

data1=spark.read.parquet("s3://asif-test1/new_cust/new1/")
#data1.show()
repartitioned_data=data1.repartition('city') 
