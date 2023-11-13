from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder.appName("BostonHousePriceAnalysis").getOrCreate()

    # Load data
    df = spark.read.csv("boston.csv", header=True, inferSchema=True)

    # Spark SQL query: Average price by number of rooms
    df.createOrReplaceTempView("house_prices")
    avg_price_by_rooms = spark.sql("SELECT RM, AVG(MEDV) as avg_price FROM house_prices GROUP BY RM")

    # Data Transformation: Filtering houses with more than 4 rooms
    houses_more_than_4_rooms = df.filter(col("RM") > 4)

    # Save results
    avg_price_by_rooms.write.csv("output/avg_price_by_rooms.csv")
    houses_more_than_4_rooms.write.csv("output/houses_more_than_4_rooms.csv")

    spark.stop()

if __name__ == "__main__":
    main()
