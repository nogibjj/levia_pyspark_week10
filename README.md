#  PySpark Project

  Welcome to my project! This repository contains all the code and resources related to the project.

## Overview
This project processes the Boston House Price dataset using PySpark. It includes a Spark SQL query and a data transformation.

## Setup
- Install dependencies: `pip install pyspark pytest`
- Download the Boston House Price dataset from Kaggle and place it in the project directory.

## Main Code
```
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
```

## Output
Average price by the number of rooms
Data of houses with more than 4 rooms


