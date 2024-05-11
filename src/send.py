import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# declare a queue
channel.queue_declare(queue='hello')

# a message can never be sent directly to a queue. Instead, it needs to go through an exchange 💼
# Think of an exchange as a mail sorting facility 📮 where all incoming mail is processed and directed to the appropriate mailboxes (queues).
# there is a default exchange denoted by ""

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()