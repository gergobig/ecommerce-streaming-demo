from pyspark.sql import SparkSession
import pyspark.sql.functions as f

SPARK = SparkSession.builder.appName('enchanced_checkouts').getOrCreate()
def main():
    read_kafka_streams()

    # streams.printSchema()

def read_kafka_streams():
    df = (
        SPARK.readStream.format('kafka')
        .options(
            **{
        'kafka.bootstrap.servers': 'kafka:9092',
        'subscribe': 'click',
    })
        .load()
    )

    df.printSchema()

    query = (
    df
    .select(f.col('key').cast('string'),f.col('value').cast('string').alias('og_value'))
    # .select('key', 'og_value')
    .writeStream.format('csv')
    # .outputMode("append")
    .option('startingOffsets', 'earliest')
    .option("checkpointLocation", "checkpoint/")
    .start('output/')
    # .trigger(processingTime='1 minute')
    # .option("failOnDataLoss", "false")
    .awaitTermination()
)





if __name__ == '__main__':
    main()