#!/bin/bash
# install java (prerequisite)
apt-get install openjdk-7-jdk -y

# install elasticsearch and logstash
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.0.deb
wget https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash_1.4.0-1-c82dc09_all.deb
dpkg -i logstash_1.4.0-1-c82dc09_all.deb
dpkg -i elasticsearch-1.1.0.deb
rm logstash_1.4.0-1-c82dc09_all.deb
rm elasticsearch-1.1.0.deb

# copy logstash.conf to /etc/logstash/conf.d and adjust rights
cp logstash.conf /etc/logstash/conf.d/
chmod root:root logstash.conf
chown 744 logstash.conf

#start services
service logstash restart
service logstash force-reload 
service elasticsearch restart
