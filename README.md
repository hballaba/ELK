# Задание соискателям на должность разработчика Python
Решение заданий отправлять на адрес Евгении Лушиной <e-lushina@it-serv.ru> в виде архива проекта, либо в виде ссылки на собственный репозиторий.
Делать форки и ветки от текущего проекта не рекомендуется. 

Дополнительное задание выполнять не обязательно, но будет плюсом.

# Задание
Разработать тесты с использованием стандартной библиотеки 
[unittest](https://docs.python.org/3/library/unittest.html "Unit testing framework").
При необходимости исправить ошибки.

Наличие предложений по доработке приветствуется.

# Дополнительное задание
Разработать [Docker Compose](https://docs.docker.com/compose/ "Overview of Docker Compose") для запуска стека 
[ELK](https://www.elastic.co/what-is/elk-stack "ELK Stack") и [Jaeger](https://www.jaegertracing.io/ "Jaeger"). 
`Jaeger` должен разворачиваться отдельными компонентами (agent, collector и query) и подключаться к Elasticsearch 
из стека ELK.

Напиши Docker Compose для запуска стека ELK и Jaeger. Jaeger должен разворачиваться отдельными компонентами (agent, collector и query) и подключаться к Elasticsearch 
из стека ELK.

Настроить Logstash для приема логов из приложения.

Подготовить тестовый пример формирующий лог и трассировку.



Для старта в первый раз необходимо запустить скрипт start.sh
В последующем достаточно команды docker-compose up

jaeger-agent помечен устаревший и не рекомендуется к использованию. https://github.com/jaegertracing/jaeger/issues/4739 
