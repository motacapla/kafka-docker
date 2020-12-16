# Tutorial
## Kafka from CLI
### Enter kafka docker container 
$ ./start-kafka-shell.sh $DOCKER_HOST_IP

### See brokers
bash-4.4# broker-list.sh

### See topics
bash-4.4# $KAFKA_HOME/bin/kafka-topics.sh --list --bootstrap-server `broker-list.sh`

### Create topic
bash-4.4# $KAFKA_HOME/bin/kafka-topics.sh --create --topic topic-from-cli --partitions 3 --replication-factor 2 --bootstrap-server `broker-list.sh` 

## Kafka from code



# References
- kafka-docker : http://wurstmeister.github.io/kafka-docker/
- KafkaからKSQLまで - dockerで簡単環境構築 : https://qiita.com/dublog/items/4b7f0d41a4075f794bd8
