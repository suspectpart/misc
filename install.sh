#!/bin/bash
# install java (prerequisite)
apt-get install openjdk-7-jdk -y

# install logstash and elasticsearch
cd /opt
wget https://download.elasticsearch.org/logstash/logstash/logstash-1.4.0.tar.gz
tar xvzf logstash-1.4.0.tar.gz
rm logstash-1.4.0.tar.gz
curl -0 https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.0.1.tar.gz
tar xvzf elasticsearch-1.0.1.tar.gz
rm elasticsearch-1.0.1.tar.gz

#start logstash
./logstash-1.4.0/bin/logstash -f logstash.conf
./elasticsearch-1.0.1/bin/elasticsearch
