FROM bitnami/spark:3.3.3
USER root

RUN apt-get update && apt-get install -y wget
RUN wget -P /usr/local/lib/python3.7/site-packages/pyspark/jars https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.13/3.3.3/spark-sql-kafka-0-10_2.13-3.3.3.jar

CMD ["spark-submit", "--jars", "spark-sql-kafka-0-10_2.13-3.3.3.jar", "/stream_processing/process.py"]
