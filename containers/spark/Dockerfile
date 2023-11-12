FROM python:3.10-bullseye as spark-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      software-properties-common \
      sudo \
      curl \
      vim \
      unzip \
      rsync \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}
ENV SCALA_HOME=${SCALA_HOME:-"/opt/scala"}

RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

RUN curl -o spark-3.3.1-bin-hadoop3.tgz https://archive.apache.org/dist/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz \
 && tar xvzf spark-3.3.1-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-3.3.1-bin-hadoop3.tgz

RUN curl -o ${SPARK_HOME}/jars/spark-sql-kafka-0-10_2.12-3.3.1.jar https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.3.1/spark-sql-kafka-0-10_2.12-3.3.1.jar \
 && curl -o ${SPARK_HOME}/jars/kafka-clients-3.3.1.jar https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.3.1/kafka-clients-3.3.1.jar \
 && curl -o ${SPARK_HOME}/jars/commons-pool2-2.12.0.jar https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.12.0/commons-pool2-2.12.0.jar  \
 && curl -o ${SPARK_HOME}/jars/spark-token-provider-kafka-0-10_2.12-3.3.1.jar https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.3.1/spark-token-provider-kafka-0-10_2.12-3.3.1.jar \
 && curl -o ${SPARK_HOME}/jars/postgresql-42.5.4 https://jdbc.postgresql.org/download/postgresql-42.5.4.jar

FROM spark-base as pyspark

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENV PATH="/opt/spark/sbin:/opt/spark/bin:${PATH}"
ENV SPARK_HOME="/opt/spark"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

COPY conf/spark-defaults.conf "$SPARK_HOME/conf"

RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]