#!/bin/bash
apt-get install openjdk-7-jdk -y
wget https://download.elasticsearch.org/logstash/logstash/logstash-1.4.0.tar.gz
tar xvzf logstash-1.4.0.tar.gz
mv logstash-1.4.0/ /opt/logstash-1.4.0
rm logstash-1.4.0.tar.gz
/opt/logstash-1.4.0/bin/logstash -e 'input { stdin { } } output { stdout { } }'
