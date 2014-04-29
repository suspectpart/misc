#!/bin/bash
# install java (prerequisite)
apt-get install openjdk-7-jdk -y
apt-get install chkconfig

# install logstash and elasticsearch
cd /opt
wget https://download.elasticsearch.org/logstash/logstash/logstash-1.4.0.tar.gz
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.0.1.tar.gz
tar xvzf logstash-1.4.0.tar.gz
tar xvzf elasticsearch-1.0.1.tar.gz
rm logstash-1.4.0.tar.gz
rm elasticsearch-1.0.1.tar.gz

# install and start elasticsearch as a service
cd elasticsearch-1.0.1/
wget --no-check-certificate 'https://github.com/elasticsearch/elasticsearch-servicewrapper/archive/master.zip' -0 elasticsearch-servicewrapper.zip
unzip elasticsearch-servicewrapper.zip
mv elasticsearch-servicewrapper-master/service bin/
rm elasticsearch-servicewrapper.zip
bin/service/elasticsearch install
chkconfig --add elasticsearch
service elasticsearch start

#start logstash
#./logstash-1.4.0/bin/logstash -f logstash.conf
#./elasticsearch-1.0.1/bin/elasticsearch
