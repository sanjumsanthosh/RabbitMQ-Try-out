import pika



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # declare a queue
    channel.queue_declare(queue='hello')

    def callback(ch,method,properties,body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello',on_message_callback=callback,auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
        exit(0)
