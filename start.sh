#!/bin/bash

# Получение образов ELC до запуска docker compose up, тк из России загрузка запрещена
docker pull elasticsearch:8.7.1
docker pull logstash:8.7.1
docker pull kibana:8.7.1
docker pull elastic/filebeat:8.7.1
docker pull elastic/metricbeat:8.7.1

# копирования файла ca.crt из контейнера es01-1
docker cp iserv-es01-1:/usr/share/elasticsearch/config/certs/ca/ca.crt /tmp/.

# Запуск docker-compose up
docker-compose up
