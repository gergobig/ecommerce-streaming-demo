from pyspark.sql import SparkSession
import pyspark.sql.functions as f

SPARK = SparkSession.builder.appName('enchanced_checkouts').getOrCreate()
def main():
    clicks = read_kafka_stream('click')
    checkouts = read_kafka_stream('checkout')

    clicks.printSchema()
    checkouts.printSchema()

def read_kafka_stream(topic_name):
    return (
        SPARK.readStream.format("kafka")
        .option(
            'kafka.bootstrap.servers',
            'kafka:9092',
        )
        .option('subscribe', topic_name)
        .load()
    )




if __name__ == '__main__':
    main()