# RabbitMQ-Try-out
Just trying out how rabbit mq works with python


| Teams    | Meaning                                         |
| -------- | ----------------------------------------------- |
| producer | A program that sends messages                   |
| queue    | A post box in RabbitMQ                          |
| consumer | A program that mostly waits to receive messages |


# Installation
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```
