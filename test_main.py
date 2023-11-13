from pyspark.sql import SparkSession
from main import main 

def test_main():
    # Setup Spark session for testing
    spark = SparkSession.builder.appName("TestBostonHousePriceAnalysis").getOrCreate()

    # Run the main function
    main()

    # Read the output data and perform assertions
    df = spark.read.csv("output/avg_price_by_rooms.csv", header=True, inferSchema=True)
    assert df.count() > 0

    df = spark.read.csv("output/houses_more_than_4_rooms.csv", header=True, inferSchema=True)
    assert df.count() > 0

    spark.stop()
