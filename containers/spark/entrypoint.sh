#!/bin/bash
SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then
    mkdir -p /opt/spark/spark-events
    start-master.sh -p 7077
elif [ "$SPARK_WORKLOAD" == "worker" ];
then
    mkdir -p /opt/spark/spark-events
    start-worker.sh spark://spark-master:7077
elif [ "$SPARK_WORKLOAD" == "history" ]
then
    mkdir -p /opt/spark/spark-events
    start-history-server.sh
fi