# reactive-microservices-with-kafka-python
Solutions to Koject's project Reactive Microservices with Kafka


## Create partition
```bash
docker exec reactive-kafka /opt/bitnami/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --topic test-topic --partitions 1 --replication-factor 1
```
